import pytest
from log_to_graph import (
    query_logs, FlowChart, node_factory,
    LIGHT_THEME, UNICORN_THEME, HOTDOG_THEME
)
from log_to_graph.flowchart.node import Node


class TestPackageIntegration:
    """Integration tests for the log_to_graph package."""

    def test_package_imports(self):
        """Test that all main package exports are available."""
        # Test function imports
        assert callable(query_logs)
        assert callable(node_factory)
        
        # Test class imports
        assert FlowChart is not None
        assert Node is not None
        
        # Test theme imports
        assert LIGHT_THEME is not None
        assert UNICORN_THEME is not None
        assert HOTDOG_THEME is not None

    def test_package_version(self):
        """Test that package version is defined."""
        import log_to_graph
        assert hasattr(log_to_graph, '__version__')
        assert isinstance(log_to_graph.__version__, str)
        assert len(log_to_graph.__version__) > 0

    def test_package_metadata(self):
        """Test that package metadata is defined."""
        import log_to_graph
        
        expected_attributes = ['__author__', '__description__']
        for attr in expected_attributes:
            assert hasattr(log_to_graph, attr)
            assert isinstance(getattr(log_to_graph, attr), str)

    def test_node_factory_integration(self, sample_event):
        """Test node_factory integration with Node classes."""
        node = node_factory(sample_event)
        
        assert isinstance(node, Node)
        assert hasattr(node, 'id')
        assert hasattr(node, 'className')
        assert hasattr(node, 'timestamp')

    def test_flowchart_integration_with_node_factory(self, sample_events_list):
        """Test FlowChart integration with node_factory."""
        # Create nodes using node_factory
        nodes = [node_factory(event) for event in sample_events_list]
        
        # Create flowchart
        flowchart = FlowChart("integration-test", nodes, LIGHT_THEME)
        
        assert flowchart.correlation_id == "integration-test"
        assert len(flowchart.nodes) == len(sample_events_list)
        assert flowchart.theme == LIGHT_THEME

    def test_theme_integration(self, sample_event):
        """Test theme integration with Node and FlowChart."""
        node = Node(sample_event)
        flowchart = FlowChart("theme-test", [node], UNICORN_THEME)
        
        # Test that theme is properly assigned
        assert flowchart.theme == UNICORN_THEME
        
        # Test that theme has required attributes
        required_theme_attrs = ['node', 'edge', 'graph', 'label']
        for attr in required_theme_attrs:
            assert hasattr(UNICORN_THEME, attr)

    def test_full_workflow_simulation(self, sample_events_list):
        """Test a complete workflow from events to flowchart."""
        # Step 1: Create nodes from events (simulating query_logs result)
        event_map = {"test-correlation": sample_events_list}
        correlation_id_list = list(event_map.keys())
        
        # Step 2: Create nodes using node_factory
        for correlation_id in correlation_id_list:
            nodes = [node_factory(event) for event in event_map[correlation_id]]
            
            # Step 3: Create flowchart
            flowchart = FlowChart(correlation_id, nodes, HOTDOG_THEME)
            
            # Step 4: Generate graphviz (mock the actual rendering)
            assert flowchart.to_graphviz() is not None

    def test_node_inheritance_compatibility(self, sample_event):
        """Test that Node subclasses work with the flowchart system."""
        # Create different types of nodes
        regular_node = node_factory(sample_event)
        
        # Test workflow node
        workflow_event = sample_event.copy()
        workflow_event["class"] = "com.starlingbank.workflow.WorkflowManager"
        workflow_node = node_factory(workflow_event)
        
        # Both should be Node instances or subclasses
        assert isinstance(regular_node, Node)
        assert isinstance(workflow_node, Node)
        
        # Both should work in a flowchart
        flowchart = FlowChart("inheritance-test", [regular_node], LIGHT_THEME)
        assert len(flowchart.nodes) == 1

    def test_error_handling_integration(self, sample_error_event):
        """Test error handling across the package."""
        # Create error node
        error_node = node_factory(sample_error_event)
        
        assert error_node.level == "ERROR"
        assert isinstance(error_node, Node)
        
        # Test in flowchart
        flowchart = FlowChart("error-test", [error_node], LIGHT_THEME)
        assert flowchart.start == error_node
        assert flowchart.end == error_node

    def test_package_all_exports(self):
        """Test that __all__ contains expected exports."""
        import log_to_graph
        
        if hasattr(log_to_graph, '__all__'):
            all_exports = log_to_graph.__all__
            
            expected_exports = [
                "query_logs", "FlowChart", "node_factory", "LIGHT_THEME"
            ]
            
            for export in expected_exports:
                assert export in all_exports, f"{export} not in __all__"
