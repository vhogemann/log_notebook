# LogToGraph Unit Tests

This directory contains comprehensive unit tests for the `log_to_graph` package.

## Test Structure

```
tests/
├── __init__.py              # Test package init
├── conftest.py              # Shared fixtures and configuration
├── test_humio.py            # Tests for Humio API integration
├── test_node.py             # Tests for Node class
├── test_node_factory.py     # Tests for node factory function
├── test_flowchart.py        # Tests for FlowChart class
├── test_theme.py            # Tests for theme system
├── test_integration.py      # Integration tests
├── run_tests.py             # Test runner script
└── README.md                # This file
```

## Running Tests

### Quick Start

```bash
# Run all tests
python tests/run_tests.py

# Or use pytest directly
pytest tests/
```

### Advanced Testing

```bash
# Run with coverage
pytest tests/ --cov=log_to_graph --cov-report=html

# Run specific test file
pytest tests/test_node.py -v

# Run specific test
pytest tests/test_node.py::TestNode::test_node_initialization_complete_event -v

# Run tests matching pattern
pytest tests/ -k "test_node" -v
```

## Test Categories

### Unit Tests
- **test_humio.py**: Tests the Humio API integration module
- **test_node.py**: Tests the base Node class functionality
- **test_node_factory.py**: Tests the node factory pattern
- **test_flowchart.py**: Tests the FlowChart visualization class
- **test_theme.py**: Tests the theme system and styling

### Integration Tests
- **test_integration.py**: Tests the complete workflow and package integration

## Test Fixtures

Common test fixtures are defined in `conftest.py`:

- `sample_event`: Standard log event for testing
- `sample_error_event`: Error-level log event
- `sample_warn_event`: Warning-level log event
- `sample_incomplete_event`: Event with missing fields
- `sample_events_list`: List of multiple events
- `mock_humio_client`: Mocked Humio client for API tests

## Coverage

Tests aim for high coverage of the `log_to_graph` package:

- **Humio Module**: API calls, error handling, data processing
- **Node Classes**: Initialization, methods, graph integration
- **FlowChart**: Graph generation, theming, edge creation
- **Node Factory**: Class detection, node type selection
- **Theme System**: Style application, color schemes

## Mocking Strategy

Tests use `unittest.mock` to isolate components:

- **HumioClient**: Mocked to avoid real API calls
- **Graphviz**: Mocked to test graph structure without rendering
- **DateTime**: Controlled for timestamp testing
- **External Dependencies**: Isolated to test core logic

## Test Data

Sample data includes:

- Complete log events with all fields
- Incomplete events missing optional fields
- Error events with stack traces
- Events from different services and groups
- Various Java class names and packages

## Development Workflow

1. **Write Tests First**: Follow TDD principles
2. **Run Tests Frequently**: Use `pytest --watch` for continuous testing
3. **Check Coverage**: Ensure new code is covered
4. **Update Fixtures**: Keep test data current with real scenarios

## Debugging Tests

```bash
# Run with pdb on failure
pytest tests/ --pdb

# Run with verbose output
pytest tests/ -vvv

# Show local variables on failure
pytest tests/ -l

# Stop on first failure
pytest tests/ -x
```

## Common Issues

### Import Errors
- Ensure `log_to_graph` package is in Python path
- Check that all `__init__.py` files exist

### Mock Configuration
- Verify mock return values match expected types
- Check that all required mock attributes are set

### Fixture Dependencies
- Ensure fixtures don't have circular dependencies
- Use appropriate fixture scopes

## Adding New Tests

When adding new functionality:

1. **Create corresponding test file** following naming convention
2. **Add fixtures** to `conftest.py` if reusable
3. **Test edge cases** and error conditions
4. **Update this README** with new test descriptions
5. **Verify coverage** includes new code

## CI/CD Integration

These tests are designed to run in CI/CD pipelines:

- **Fast execution**: Mocked external dependencies
- **Deterministic**: Controlled time and randomness
- **Comprehensive**: High coverage and edge cases
- **Clear output**: Detailed failure information

For CI integration, run:

```bash
pytest tests/ --junitxml=test-results.xml --cov=log_to_graph --cov-report=xml
```
