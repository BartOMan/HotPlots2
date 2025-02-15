# Testing Documentation

This project uses pytest for testing. The tests are designed to run both locally and in CI/CD pipelines on GitHub.

## Running Tests Locally

1. First, install the package and test dependencies:
   ```bash
   pip install -e ".[test]"
   ```

2. Run the tests:
   ```bash
   pytest
   ```

   This will:
   - Run all tests
   - Generate a coverage report
   - Show test results in the terminal

3. View the coverage report:
   - Open `htmlcov/index.html` in your browser to see detailed coverage information

## Test Configuration

- Tests are located in the `tests/` directory
- `conftest.py` contains shared fixtures
- `pytest.ini` contains pytest configuration
- Coverage reports are generated automatically

## GitHub Actions Integration

Tests automatically run on GitHub when:
- Pushing to the main branch
- Creating a pull request to the main branch

The workflow:
1. Runs on Ubuntu with Python 3.8, 3.9, and 3.10
2. Installs dependencies
3. Runs tests
4. Uploads coverage reports to Codecov

### Viewing GitHub Results

1. Go to your repository's "Actions" tab to see test results
2. Click on any workflow run to see detailed test output
3. Coverage reports are available on Codecov (requires setup)

## Test Structure

The tests are organized into classes and functions:
- `TestPlotManager`: Main test class for PlotManager
- Individual test methods for each functionality
- Fixtures in `conftest.py` provide test setup

## Adding New Tests

When adding new features:
1. Create test functions in `test_plot_manager.py`
2. Use the `plot_manager` fixture for PlotManager instances
3. Follow the existing naming convention: `test_*`
4. Include assertions to verify expected behavior

## Common Issues

1. **Missing Dependencies**
   ```bash
   pip install -e ".[test]"
   ```

2. **Backend Issues**
   - Tests use the 'Agg' backend for non-interactive testing
   - Configured in `conftest.py`

3. **Coverage Reports**
   - If htmlcov directory is missing, run:
   ```bash
   pytest --cov=src --cov-report=html
   ``` 