import pytest
from unittest.mock import Mock, patch
from log_to_graph.humio import query_logs


class TestHumioModule:
    """Test cases for the Humio module."""

    @patch('log_to_graph.humio.HumioClient')
    def test_query_logs_success(self, mock_humio_client_class, mock_humio_client):
        """Test successful log querying from Humio."""
        # Setup
        mock_humio_client_class.return_value = mock_humio_client
        user_token = "test-token"
        repo = "test-repo"
        start = "1h"
        correlation_id = "test-correlation-id"

        # Execute
        result = query_logs(user_token, repo, start, correlation_id)

        # Assert
        mock_humio_client_class.assert_called_once_with(
            base_url="https://cloud.humio.com",
            repository=repo,
            user_token=user_token
        )
        mock_humio_client.create_queryjob.assert_called_once_with(
            f" join({{{correlation_id} class=* service=*}}, field=correlation_id)",
            is_live=False,
            start=start
        )
        assert isinstance(result, dict)
        assert "test-correlation-id" in result
        assert len(result["test-correlation-id"]) == 1

    @patch('log_to_graph.humio.HumioClient')
    def test_query_logs_multiple_events(self, mock_humio_client_class, sample_events_list):
        """Test querying multiple events with different correlation IDs."""
        # Setup
        mock_client = Mock()
        mock_humio_client_class.return_value = mock_client
        
        # Create events with different correlation IDs
        events = [
            {"correlation_id": "id1", "message": "event1"},
            {"correlation_id": "id2", "message": "event2"},
            {"correlation_id": "id1", "message": "event3"}
        ]
        
        mock_queryjob = Mock()
        mock_poll_result = Mock()
        mock_poll_result.events = events
        mock_queryjob.poll_until_done.return_value = [mock_poll_result]
        mock_client.create_queryjob.return_value = mock_queryjob

        # Execute
        result = query_logs("token", "repo", "1h", "test-id")

        # Assert
        assert len(result) == 2
        assert "id1" in result
        assert "id2" in result
        assert len(result["id1"]) == 2
        assert len(result["id2"]) == 1

    @patch('log_to_graph.humio.HumioClient')
    def test_query_logs_empty_result(self, mock_humio_client_class):
        """Test querying when no events are found."""
        # Setup
        mock_client = Mock()
        mock_humio_client_class.return_value = mock_client
        
        mock_queryjob = Mock()
        mock_poll_result = Mock()
        mock_poll_result.events = []
        mock_queryjob.poll_until_done.return_value = [mock_poll_result]
        mock_client.create_queryjob.return_value = mock_queryjob

        # Execute
        result = query_logs("token", "repo", "1h", "nonexistent-id")

        # Assert
        assert isinstance(result, dict)
        assert len(result) == 0

    @patch('log_to_graph.humio.HumioClient')
    def test_query_logs_with_different_params(self, mock_humio_client_class, mock_humio_client):
        """Test query_logs with different parameter combinations."""
        # Setup
        mock_humio_client_class.return_value = mock_humio_client
        
        test_cases = [
            ("token1", "sb-demo", "12h", "correlation-1"),
            ("token2", "sb-production", "7d", "correlation-2"),
            ("token3", "test-repo", "30d", "correlation-3")
        ]

        for user_token, repo, start, correlation_id in test_cases:
            # Execute
            result = query_logs(user_token, repo, start, correlation_id)
            
            # Assert
            mock_humio_client_class.assert_called_with(
                base_url="https://cloud.humio.com",
                repository=repo,
                user_token=user_token
            )
            mock_humio_client.create_queryjob.assert_called_with(
                f" join({{{correlation_id} class=* service=*}}, field=correlation_id)",
                is_live=False,
                start=start
            )

    def test_query_logs_type_hints(self):
        """Test that the function has correct type hints."""
        import inspect
        sig = inspect.signature(query_logs)
        
        # Check parameter types
        assert sig.parameters['user_token'].annotation == str
        assert sig.parameters['repo'].annotation == str
        assert sig.parameters['start'].annotation == str
        assert sig.parameters['correlation_id'].annotation == str
        
        # Check return type
        assert str(sig.return_annotation) == "dict[str, list]"
