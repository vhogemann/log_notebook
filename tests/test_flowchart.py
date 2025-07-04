import pytest
from unittest.mock import Mock, patch, MagicMock
from log_to_graph.flowchart.flowchart import FlowChart
from log_to_graph.flowchart.node.node import Node
from log_to_graph.flowchart.theme.theme import Theme


class TestFlowChart:
    """Test cases for the FlowChart class."""

    @pytest.fixture
    def mock_nodes(self, sample_events_list):
        """Create mock nodes with different timestamps."""
        nodes = []
        timestamps = [1000, 2000, 3000]  # Different timestamps for ordering
        
        for i, event in enumerate(sample_events_list):
            event["@timestamp"] = timestamps[i]
            node = Node(event)
            nodes.append(node)
        
        return nodes

    @pytest.fixture
    def mock_theme(self):
        """Create a mock theme for testing."""
        theme = Mock()
        
        # Graph attributes
        theme.label.fontsize = "12"
        theme.label.fontname = "Arial"
        theme.label.bgcolor = "white"
        theme.graph.bgcolor = "white"
        theme.graph.fontcolor = "black"
        theme.graph.fontname = "Arial"
        
        # Node attributes
        theme.node.shape = "rectangle"
        theme.node.style = "filled"
        theme.node.fillcolor = "lightblue"
        theme.node.fontcolor = "black"
        theme.node.fontname = "Arial"
        theme.node.fontsize = "10"
        
        # Edge attributes
        theme.edge.color = "black"
        
        # Start/End node attributes
        theme.start.shape = "circle"
        theme.start.style = "filled"
        theme.start.fillcolor = "green"
        theme.start.fontname = "Arial"
        theme.start.fontsize = "10"
        theme.start.fontcolor = "white"
        
        theme.end.shape = "circle"
        theme.end.style = "filled"
        theme.end.fillcolor = "red"
        theme.end.fontname = "Arial"
        theme.end.fontsize = "10"
        theme.end.fontcolor = "white"
        
        # Group and service colors
        theme.group_colors = [("lightgray", "gray"), ("lightblue", "blue")]
        theme.service_colors = [("white", "black"), ("lightyellow", "orange")]
        
        return theme

    def test_get_edges_ordering(self, mock_nodes):
        """Test that _get_edges properly orders nodes by timestamp."""
        # Shuffle the nodes to test ordering
        shuffled_nodes = [mock_nodes[2], mock_nodes[0], mock_nodes[1]]
        
        edges = FlowChart._get_edges(shuffled_nodes)
        
        # Should return edges in timestamp order
        assert len(edges) == 2
        assert edges[0][0].timestamp < edges[0][1].timestamp
        assert edges[1][0].timestamp < edges[1][1].timestamp
        
        # Verify the sequence
        assert edges[0][0].timestamp == 1000
        assert edges[0][1].timestamp == 2000
        assert edges[1][0].timestamp == 2000
        assert edges[1][1].timestamp == 3000

    def test_get_edges_single_node(self, sample_event):
        """Test _get_edges with single node returns empty list."""
        node = Node(sample_event)
        edges = FlowChart._get_edges([node])
        
        assert edges == []

    def test_get_edges_empty_list(self):
        """Test _get_edges with empty list returns empty list."""
        edges = FlowChart._get_edges([])
        assert edges == []

    def test_flowchart_initialization(self, mock_nodes, mock_theme):
        """Test FlowChart initialization."""
        correlation_id = "test-correlation-id"
        
        flowchart = FlowChart(correlation_id, mock_nodes, mock_theme)
        
        assert flowchart.correlation_id == correlation_id
        assert flowchart.nodes == mock_nodes
        assert flowchart.theme == mock_theme
        assert len(flowchart.edges) == 2
        assert flowchart.start == mock_nodes[0]  # First by timestamp
        assert flowchart.end == mock_nodes[-1]   # Last by timestamp

    def test_flowchart_default_theme(self, mock_nodes):
        """Test FlowChart initialization with default theme."""
        from log_to_graph.flowchart.theme import DEFAULT_THEME
        
        flowchart = FlowChart("test-id", mock_nodes)
        
        assert flowchart.theme == DEFAULT_THEME

    def test_get_subgraph_colors(self, mock_nodes, mock_theme):
        """Test _get_subgraph_colors method."""
        flowchart = FlowChart("test-id", mock_nodes, mock_theme)
        
        # Test consistent color assignment
        color1 = flowchart._get_subgraph_colors("service1", mock_theme.group_colors)
        color2 = flowchart._get_subgraph_colors("service1", mock_theme.group_colors)
        color3 = flowchart._get_subgraph_colors("service2", mock_theme.group_colors)
        
        # Same service should get same color
        assert color1 == color2
        
        # Different services may get different colors
        assert color1 in mock_theme.group_colors
        assert color3 in mock_theme.group_colors

    @patch('log_to_graph.flowchart.flowchart.Digraph')
    def test_to_graphviz_basic_structure(self, mock_digraph_class, mock_nodes, mock_theme):
        """Test basic structure of to_graphviz method."""
        # Setup
        mock_graph = Mock()
        mock_digraph_class.return_value = mock_graph
        mock_subgraph = Mock()
        mock_graph.subgraph.return_value.__enter__.return_value = mock_subgraph
        mock_subgraph.subgraph.return_value.__enter__.return_value = mock_subgraph
        
        flowchart = FlowChart("test-correlation-id", mock_nodes, mock_theme)
        
        # Execute
        result = flowchart.to_graphviz()
        
        # Assert
        assert result == mock_graph
        
        # Verify graph initialization
        mock_digraph_class.assert_called_once_with(
            format='svg', 
            engine='dot', 
            graph_attr={'splines':'ortho'}
        )
        
        # Verify graph attributes were set
        assert mock_graph.attr.call_count >= 3  # label, graph, node, edge attrs

    @patch('log_to_graph.flowchart.flowchart.Digraph')
    def test_to_graphviz_start_end_nodes(self, mock_digraph_class, mock_nodes, mock_theme):
        """Test that start and end nodes are added."""
        # Setup
        mock_graph = Mock()
        mock_digraph_class.return_value = mock_graph
        mock_subgraph = Mock()
        mock_graph.subgraph.return_value.__enter__.return_value = mock_subgraph
        mock_subgraph.subgraph.return_value.__enter__.return_value = mock_subgraph
        
        flowchart = FlowChart("test-correlation-id", mock_nodes, mock_theme)
        
        # Execute
        result = flowchart.to_graphviz()
        
        # Verify start and end nodes were added
        node_calls = mock_graph.node.call_args_list
        
        # Should have start node ('S') and end node ('E')
        start_call = None
        end_call = None
        
        for call in node_calls:
            if call[0][0] == 'S':
                start_call = call
            elif call[0][0] == 'E':
                end_call = call
        
        assert start_call is not None
        assert end_call is not None
        assert start_call[0][1] == 'start'
        assert end_call[0][1] == 'end'

    @patch('log_to_graph.flowchart.flowchart.Digraph')
    def test_to_graphviz_edges(self, mock_digraph_class, mock_nodes, mock_theme):
        """Test that edges are added between nodes."""
        # Setup
        mock_graph = Mock()
        mock_digraph_class.return_value = mock_graph
        mock_subgraph = Mock()
        mock_graph.subgraph.return_value.__enter__.return_value = mock_subgraph
        mock_subgraph.subgraph.return_value.__enter__.return_value = mock_subgraph
        
        flowchart = FlowChart("test-correlation-id", mock_nodes, mock_theme)
        
        # Execute
        result = flowchart.to_graphviz()
        
        # Verify edges were added
        edge_calls = mock_graph.edge.call_args_list
        
        # Should have at least:
        # - Start to first node
        # - Node to node edges (based on flowchart.edges)
        # - Last node to end
        assert len(edge_calls) >= 3
        
        # Check start edge
        start_edge = edge_calls[0]
        assert start_edge[0][0] == 'S'
        assert start_edge[0][1] == str(flowchart.start.id)
        
        # Check end edge
        end_edge = edge_calls[-1]
        assert end_edge[0][0] == str(flowchart.end.id)
        assert end_edge[0][1] == 'E'

    @patch('log_to_graph.flowchart.flowchart.Digraph')
    def test_to_graphviz_subgraphs(self, mock_digraph_class, mock_nodes, mock_theme):
        """Test that subgraphs are created for groups and services."""
        # Setup
        mock_graph = Mock()
        mock_digraph_class.return_value = mock_graph
        mock_subgraph = Mock()
        mock_service_subgraph = Mock()
        
        # Setup nested subgraph context managers
        mock_graph.subgraph.return_value.__enter__ = Mock(return_value=mock_subgraph)
        mock_graph.subgraph.return_value.__exit__ = Mock(return_value=None)
        mock_subgraph.subgraph.return_value.__enter__ = Mock(return_value=mock_service_subgraph)
        mock_subgraph.subgraph.return_value.__exit__ = Mock(return_value=None)
        
        flowchart = FlowChart("test-correlation-id", mock_nodes, mock_theme)
        
        # Execute
        result = flowchart.to_graphviz()
        
        # Verify subgraphs were created
        assert mock_graph.subgraph.call_count == len(mock_nodes)
        assert mock_subgraph.subgraph.call_count == len(mock_nodes)

    def test_flowchart_correlation_id_in_label(self, mock_nodes, mock_theme):
        """Test that correlation ID appears in the graph label."""
        correlation_id = "special-test-id-123"
        
        with patch('log_to_graph.flowchart.flowchart.Digraph') as mock_digraph_class:
            mock_graph = Mock()
            mock_digraph_class.return_value = mock_graph
            mock_subgraph = Mock()
            mock_graph.subgraph.return_value.__enter__.return_value = mock_subgraph
            mock_subgraph.subgraph.return_value.__enter__.return_value = mock_subgraph
            
            flowchart = FlowChart(correlation_id, mock_nodes, mock_theme)
            result = flowchart.to_graphviz()
            
            # Check that attr was called with the correlation ID in label
            attr_calls = mock_graph.attr.call_args_list
            label_call = attr_calls[0]  # First call should be for label
            
            assert f'Correlation ID: {correlation_id}' in str(label_call)

    def test_flowchart_single_node(self, sample_event, mock_theme):
        """Test FlowChart with single node."""
        node = Node(sample_event)
        
        flowchart = FlowChart("single-node-test", [node], mock_theme)
        
        assert flowchart.start == node
        assert flowchart.end == node
        assert len(flowchart.edges) == 0
        assert len(flowchart.nodes) == 1

    def test_flowchart_empty_nodes_raises_error(self, mock_theme):
        """Test that FlowChart raises error with empty nodes list."""
        with pytest.raises(IndexError):
            FlowChart("empty-test", [], mock_theme)

    def test_flowchart_nodes_modification_after_init(self, mock_nodes, mock_theme):
        """Test that FlowChart sorts nodes internally and doesn't modify original list."""
        original_order = [node.timestamp for node in mock_nodes]
        
        # Shuffle nodes
        shuffled_nodes = [mock_nodes[2], mock_nodes[0], mock_nodes[1]]
        
        flowchart = FlowChart("test-id", shuffled_nodes, mock_theme)
        
        # Original list should be unchanged
        assert [node.timestamp for node in shuffled_nodes] == [3000, 1000, 2000]
        
        # FlowChart should have sorted nodes
        assert flowchart.start.timestamp == 1000
        assert flowchart.end.timestamp == 3000
