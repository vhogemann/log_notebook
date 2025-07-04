import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Sample event data for testing
SAMPLE_EVENT = {
    "@timestamp": int(datetime.now().timestamp() * 1000),
    "class": "com.starlingbank.test.TestClass",
    "level": "INFO",
    "message": "Test message",
    "service": "test-service",
    "engineering_group": "Test Group",
    "correlation_id": "test-correlation-id"
}

SAMPLE_ERROR_EVENT = {
    "@timestamp": int(datetime.now().timestamp() * 1000),
    "class": "com.starlingbank.test.ErrorClass",
    "level": "ERROR",
    "message": "Error occurred\nat com.starlingbank.test.ErrorClass.method1(ErrorClass.java:10)\nat com.starlingbank.test.ErrorClass.method2(ErrorClass.java:20)",
    "service": "error-service",
    "engineering_group": "Error Group",
    "correlation_id": "error-correlation-id"
}

SAMPLE_WARN_EVENT = {
    "@timestamp": int(datetime.now().timestamp() * 1000),
    "class": "com.starlingbank.test.WarnClass",
    "level": "WARN",
    "message": "Warning message\nat com.starlingbank.test.WarnClass.warnMethod(WarnClass.java:15)",
    "service": "warn-service",
    "engineering_group": "Warn Group",
    "correlation_id": "warn-correlation-id"
}

SAMPLE_INCOMPLETE_EVENT = {
    "@timestamp": int(datetime.now().timestamp() * 1000),
    "message": "Message without class or level",
    "service": "incomplete-service",
    "engineering_group": "Incomplete Group",
    "correlation_id": "incomplete-correlation-id"
}

@pytest.fixture
def sample_event():
    """Fixture providing a standard sample event."""
    return SAMPLE_EVENT.copy()

@pytest.fixture
def sample_error_event():
    """Fixture providing a sample error event."""
    return SAMPLE_ERROR_EVENT.copy()

@pytest.fixture
def sample_warn_event():
    """Fixture providing a sample warning event."""
    return SAMPLE_WARN_EVENT.copy()

@pytest.fixture
def sample_incomplete_event():
    """Fixture providing an incomplete event."""
    return SAMPLE_INCOMPLETE_EVENT.copy()

@pytest.fixture
def sample_events_list():
    """Fixture providing a list of sample events."""
    return [
        SAMPLE_EVENT.copy(),
        SAMPLE_ERROR_EVENT.copy(),
        SAMPLE_WARN_EVENT.copy()
    ]

@pytest.fixture
def mock_humio_client():
    """Fixture providing a mocked HumioClient."""
    mock_client = Mock()
    mock_queryjob = Mock()
    mock_poll_result = Mock()
    
    # Configure the mock poll result
    mock_poll_result.events = [SAMPLE_EVENT.copy()]
    mock_queryjob.poll_until_done.return_value = [mock_poll_result]
    mock_client.create_queryjob.return_value = mock_queryjob
    
    return mock_client
