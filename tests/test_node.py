import pytest
import uuid
from datetime import datetime
from unittest.mock import Mock, patch
from log_to_graph.flowchart.node.node import Node


class TestNode:
    """Test cases for the Node class."""

    def test_node_initialization_complete_event(self, sample_event):
        """Test Node initialization with complete event data."""
        node = Node(sample_event)
        
        assert node.className == "TestClass"
        assert node.packageName == "com.starlingbank.test"
        assert node.level == "INFO"
        assert node.timestamp == sample_event["@timestamp"]
        assert node.message == sample_event["message"]
        assert node.service == sample_event["service"]
        assert node.group == sample_event["engineering_group"].lower()
        assert node.correlation_id == sample_event["correlation_id"]
        assert isinstance(node.id, str)
        assert len(node.id) == 36  # UUID length

    def test_node_initialization_incomplete_event(self, sample_incomplete_event):
        """Test Node initialization with incomplete event data."""
        node = Node(sample_incomplete_event)
        
        assert node.className == "Unknown"
        assert node.packageName == "unknown"
        assert node.level == "INFO"  # Default level
        assert node.timestamp == sample_incomplete_event["@timestamp"]
        assert node.message == sample_incomplete_event["message"]

    def test_class_name_extraction(self):
        """Test _class_name static method."""
        test_cases = [
            ("com.starlingbank.test.TestClass", "TestClass"),
            ("com.example.service.MyService", "MyService"),
            ("SimpleClass", "SimpleClass"),
            ("", ""),
        ]
        
        for full_class, expected in test_cases:
            result = Node._class_name(full_class)
            assert result == expected

    def test_package_name_extraction(self, sample_event):
        """Test _package_name method."""
        node = Node(sample_event)
        
        test_cases = [
            ("com.starlingbank.test.TestClass", "com.starlingbank.test"),
            ("com.example.MyClass", "com.example"),
            ("SimpleClass", ""),
            ("", ""),
        ]
        
        for full_class, expected in test_cases:
            result = node._package_name(full_class)
            assert result == expected

    @patch('log_to_graph.flowchart.node.node.datetime')
    def test_format_timestamp(self, mock_datetime):
        """Test timestamp formatting."""
        # Mock current time
        mock_now = datetime(2023, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = mock_now
        mock_datetime.fromtimestamp.return_value = datetime(2023, 1, 1, 11, 0, 0)
        
        # Test timestamp from 1 hour ago
        timestamp = int(datetime(2023, 1, 1, 11, 0, 0).timestamp() * 1000)
        
        with patch('log_to_graph.flowchart.node.node.humanize.precisedelta', return_value="1 hour"):
            result = Node._format_timestamp(timestamp)
            assert result == "1 hour ago"

    def test_stacktrace_extraction_with_starlingbank_code(self, sample_error_event):
        """Test stacktrace extraction filtering for Starling Bank code."""
        node = Node(sample_error_event)
        stacktrace = node.stacktrace()
        
        assert "com.starlingbank.test.ErrorClass.method1" in stacktrace
        assert "com.starlingbank.test.ErrorClass.method2" in stacktrace
        assert stacktrace.count("at com.starlingbank") == 2

    def test_stacktrace_with_non_starlingbank_code(self):
        """Test stacktrace filtering with non-Starling Bank code."""
        event_with_external_stack = {
            "@timestamp": int(datetime.now().timestamp() * 1000),
            "class": "com.starlingbank.test.TestClass",
            "level": "ERROR",
            "message": "Error\nat com.starlingbank.internal.Method.call(Method.java:10)\nat java.lang.Thread.run(Thread.java:748)\nat com.starlingbank.another.Method.call(Another.java:20)",
            "service": "test-service",
            "engineering_group": "Test",
            "correlation_id": "test-id"
        }
        
        node = Node(event_with_external_stack)
        stacktrace = node.stacktrace()
        
        assert "com.starlingbank.internal.Method.call" in stacktrace
        assert "com.starlingbank.another.Method.call" in stacktrace
        assert "java.lang.Thread.run" not in stacktrace
        assert "..." in stacktrace

    def test_label_generation(self, sample_event):
        """Test HTML label generation for nodes."""
        node = Node(sample_event)
        label = node.label()
        
        assert "<TABLE" in label
        assert node.packageName in label
        assert node.className in label
        assert "FONT POINT-SIZE" in label

    def test_string_representation(self, sample_event):
        """Test string representation of Node."""
        node = Node(sample_event)
        assert str(node) == node.className

    def test_linecolor_selection(self, sample_event, sample_error_event, sample_warn_event):
        """Test line color selection based on log level."""
        mock_theme = Mock()
        mock_theme.error_edge.color = "red"
        mock_theme.warn_edge.color = "orange"
        mock_theme.info_edge.color = "blue"
        mock_theme.edge.color = "black"
        
        # Test INFO level
        info_node = Node(sample_event)
        assert info_node._linecolor(mock_theme) == "blue"
        
        # Test ERROR level
        error_node = Node(sample_error_event)
        assert error_node._linecolor(mock_theme) == "red"
        
        # Test WARN level
        warn_node = Node(sample_warn_event)
        assert warn_node._linecolor(mock_theme) == "orange"
        
        # Test unknown level
        unknown_event = sample_event.copy()
        unknown_event["level"] = "UNKNOWN"
        unknown_node = Node(unknown_event)
        assert unknown_node._linecolor(mock_theme) == "black"

    def test_add_note_method(self, sample_event):
        """Test addNote method (should be overrideable)."""
        node = Node(sample_event)
        mock_theme = Mock()
        mock_graph = Mock()
        
        # Should not raise an exception
        result = node.addNote(mock_theme, mock_graph)
        assert result is None

    def test_add_to_graph_info_level(self, sample_event):
        """Test adding INFO level node to graph."""
        node = Node(sample_event)
        mock_theme = Mock()
        mock_graph = Mock()
        mock_subgraph = Mock()
        
        # Setup theme attributes
        mock_theme.node.shape = "rectangle"
        mock_theme.node.style = "filled"
        mock_theme.node.fillcolor = "lightblue"
        mock_theme.node.fontname = "Arial"
        mock_theme.node.fontsize = "10"
        mock_theme.node.fontcolor = "black"
        mock_theme.info_edge.color = "blue"
        
        result = node.addToGraph(mock_theme, mock_graph, mock_subgraph)
        
        # Verify node was added to subgraph
        mock_subgraph.node.assert_called_once()
        call_args = mock_subgraph.node.call_args
        assert call_args[0][0] == str(node.id)  # node ID
        assert "shape" in call_args[1]
        assert call_args[1]["shape"] == "rectangle"

    def test_add_to_graph_error_level(self, sample_error_event):
        """Test adding ERROR level node to graph with error note."""
        node = Node(sample_error_event)
        mock_theme = Mock()
        mock_graph = Mock()
        mock_subgraph = Mock()
        
        # Setup theme attributes for error
        mock_theme.node.shape = "rectangle"
        mock_theme.node.style = "filled"
        mock_theme.node.fillcolor = "lightblue"
        mock_theme.node.fontname = "Arial"
        mock_theme.node.fontsize = "10"
        mock_theme.node.fontcolor = "black"
        mock_theme.error_edge.color = "red"
        mock_theme.error_edge.style = "solid"
        mock_theme.error_note.shape = "note"
        mock_theme.error_note.style = "filled"
        mock_theme.error_note.fillcolor = "pink"
        mock_theme.error_note.fontname = "Arial"
        mock_theme.error_note.fontsize = "8"
        mock_theme.error_note.fontcolor = "red"
        
        result = node.addToGraph(mock_theme, mock_graph, mock_subgraph)
        
        # Verify main node was added to subgraph
        mock_subgraph.node.assert_called_once()
        
        # Verify error note was added to main graph
        mock_graph.node.assert_called_once()
        error_call_args = mock_graph.node.call_args
        assert error_call_args[0][0] == f"{node.id}_error"
        
        # Verify edge between node and error note
        mock_subgraph.edge.assert_called_once()
        edge_call_args = mock_subgraph.edge.call_args
        assert edge_call_args[0][0] == str(node.id)
        assert edge_call_args[0][1] == f"{node.id}_error"

    def test_add_to_graph_warn_level(self, sample_warn_event):
        """Test adding WARN level node to graph with warning note."""
        node = Node(sample_warn_event)
        mock_theme = Mock()
        mock_graph = Mock()
        mock_subgraph = Mock()
        
        # Setup theme attributes for warning
        mock_theme.node.shape = "rectangle"
        mock_theme.node.style = "filled"
        mock_theme.node.fillcolor = "lightblue"
        mock_theme.node.fontname = "Arial"
        mock_theme.node.fontsize = "10"
        mock_theme.node.fontcolor = "black"
        mock_theme.warn_edge.color = "orange"
        mock_theme.warn_edge.style = "solid"
        mock_theme.warn_note.shape = "note"
        mock_theme.warn_note.style = "filled"
        mock_theme.warn_note.fillcolor = "lightyellow"
        mock_theme.warn_note.fontname = "Arial"
        mock_theme.warn_note.fontsize = "8"
        mock_theme.warn_note.fontcolor = "orange"
        
        result = node.addToGraph(mock_theme, mock_graph, mock_subgraph)
        
        # Verify main node was added to subgraph
        mock_subgraph.node.assert_called_once()
        
        # Verify warning note was added to main graph
        mock_graph.node.assert_called_once()
        warn_call_args = mock_graph.node.call_args
        assert warn_call_args[0][0] == f"{node.id}_warn"
        
        # Verify edge between node and warning note
        mock_subgraph.edge.assert_called_once()

    def test_node_unique_ids(self, sample_event):
        """Test that each node gets a unique ID."""
        node1 = Node(sample_event)
        node2 = Node(sample_event)
        
        assert node1.id != node2.id
        assert len(node1.id) == 36  # UUID4 length
        assert len(node2.id) == 36  # UUID4 length

    def test_relative_time_property(self, sample_event):
        """Test that relative_time is set during initialization."""
        node = Node(sample_event)
        
        assert hasattr(node, 'relative_time')
        assert isinstance(node.relative_time, str)
        assert "ago" in node.relative_time
