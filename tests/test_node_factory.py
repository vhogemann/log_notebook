import pytest
from unittest.mock import Mock, patch
from log_to_graph.flowchart.node.node_factory import node_factory
from log_to_graph.flowchart.node.node import Node


class TestNodeFactory:
    """Test cases for the node_factory function."""

    def test_node_factory_default_node(self, sample_event):
        """Test factory creates default Node for unknown class."""
        result = node_factory(sample_event)
        
        assert isinstance(result, Node)
        assert result.className == "TestClass"
        assert result.level == "INFO"

    def test_node_factory_no_class(self, sample_incomplete_event):
        """Test factory creates default Node when class is missing."""
        result = node_factory(sample_incomplete_event)
        
        assert isinstance(result, Node)
        assert result.className == "Unknown"

    @patch('log_to_graph.flowchart.node.node_factory.WorkflowManagerNode')
    def test_node_factory_workflow_manager(self, mock_workflow_node, sample_event):
        """Test factory creates WorkflowManagerNode for WorkflowManager class."""
        # Setup
        sample_event["class"] = "com.starlingbank.workflow.WorkflowManager"
        mock_instance = Mock()
        mock_workflow_node.return_value = mock_instance
        
        # Execute
        result = node_factory(sample_event)
        
        # Assert
        mock_workflow_node.assert_called_once_with(sample_event)
        assert result == mock_instance

    @patch('log_to_graph.flowchart.node.node_factory.AuthRequestSaveHandler')
    def test_node_factory_auth_request_save_handler(self, mock_auth_handler, sample_event):
        """Test factory creates AuthRequestSaveHandler for specific class."""
        # Setup
        sample_event["class"] = "com.starlingbank.cardprocessor.workflow.auth.handlers.AuthRequestSaveHandler"
        mock_instance = Mock()
        mock_auth_handler.return_value = mock_instance
        
        # Execute
        result = node_factory(sample_event)
        
        # Assert
        mock_auth_handler.assert_called_once_with(sample_event)
        assert result == mock_instance

    def test_node_factory_unknown_starlingbank_class(self, sample_event):
        """Test factory creates default Node for unknown Starling Bank class."""
        sample_event["class"] = "com.starlingbank.unknown.UnknownClass"
        
        result = node_factory(sample_event)
        
        assert isinstance(result, Node)
        assert result.className == "UnknownClass"

    def test_node_factory_external_class(self, sample_event):
        """Test factory creates default Node for external classes."""
        sample_event["class"] = "org.springframework.web.Controller"
        
        result = node_factory(sample_event)
        
        assert isinstance(result, Node)
        assert result.className == "Controller"

    def test_node_factory_preserves_event_data(self, sample_event):
        """Test that factory preserves all event data in created nodes."""
        original_data = sample_event.copy()
        
        result = node_factory(sample_event)
        
        # Verify the original event data is preserved
        assert result.message == original_data["message"]
        assert result.service == original_data["service"]
        assert result.correlation_id == original_data["correlation_id"]
        assert result.timestamp == original_data["@timestamp"]

    def test_node_factory_edge_cases(self):
        """Test node factory with edge case inputs."""
        edge_cases = [
            {"class": None},  # None class
            {"class": ""},    # Empty class
            {},               # Empty event
        ]
        
        for event in edge_cases:
            # Add required fields
            event.update({
                "@timestamp": 1234567890000,
                "message": "test",
                "service": "test",
                "engineering_group": "test",
                "correlation_id": "test"
            })
            
            result = node_factory(event)
            assert isinstance(result, Node)

    def test_node_factory_case_sensitivity(self, sample_event):
        """Test that factory is case-sensitive for class matching."""
        # Test with different case
        sample_event["class"] = "com.starlingbank.workflow.workflowmanager"  # lowercase
        
        result = node_factory(sample_event)
        
        # Should create default Node, not WorkflowManagerNode
        assert isinstance(result, Node)
        assert result.className == "workflowmanager"

    def test_node_factory_partial_class_match(self, sample_event):
        """Test that factory requires exact class match."""
        # Test with partial match
        sample_event["class"] = "com.starlingbank.workflow.WorkflowManagerTest"
        
        result = node_factory(sample_event)
        
        # Should create default Node, not WorkflowManagerNode
        assert isinstance(result, Node)
        assert result.className == "WorkflowManagerTest"

    def test_node_factory_return_types(self, sample_event):
        """Test that all factory returns are Node instances or subclasses."""
        test_classes = [
            "com.starlingbank.workflow.WorkflowManager",
            "com.starlingbank.cardprocessor.workflow.auth.handlers.AuthRequestSaveHandler",
            "com.starlingbank.test.TestClass",
            "org.external.SomeClass"
        ]
        
        for class_name in test_classes:
            event = sample_event.copy()
            event["class"] = class_name
            
            result = node_factory(event)
            
            # All results should be Node instances or subclasses
            assert isinstance(result, Node)
