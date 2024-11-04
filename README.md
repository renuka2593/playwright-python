# playwright-python

[![Pylint](https://github.com/renuka2593/playwright-python/actions/workflows/pylint.yml/badge.svg)](https://github.com/renuka2593/playwright-python/actions/workflows/pylint.yml)

### Prerequisites

* Python 3.7 or higher
* PyCharm or Any IDE

### Install Playwright and Required Browsers

First, make sure Playwright and the necessary browser dependencies are installed. Run the following commands:

```bash
pip install -r requirements.txt
python -m playwright install
```

* `pip install playwright` installs the Playwright library, allowing you to write and execute browser-based tests.
* `playwright install` downloads browser dependencies, such as Chromium, Firefox, and WebKit, which are required for
  Playwright to run tests across different browsers.
* `pytest` is a testing framework that makes it easy to write simple and scalable test cases. It provides powerful
  features such as fixtures, parameterized tests, and plugins.
* `pytest-playwright` integrates Playwright with pytest, allowing you to run Playwright tests with pytest's
  capabilities, including test discovery, execution, and reporting.

### Run with pytest

```bash
pytest test_login.py
```

### Features

1. **Page Object Model (POM)**: Implements the Page Object Model for better organization and maintainability of test
   code.
2. **Parameterization** : Utilizes parameterized tests to validate multiple login scenarios.
3. **Cross-Browser Testing** : Supports testing across different browsers (Chromium, Firefox, WebKit).
4. **Integration with Pytest**: Leverages the Pytest framework for running tests and generating reports.

### Notes 
* **Use `test_` Prefix**: Always use the test_ prefix for your test methods and functions. This tells pytest to recognize them as test cases during test discovery.
* **Fixture Usage**: Ensure that you have the necessary fixtures defined (e.g., page, browser, context) for your tests. These fixtures are essential for setting up the environment and are provided by pytest-playwright.
* **Error Handling**: If you encounter errors related to missing fixtures (like fixture 'page' not found), check that pytest-playwright is properly installed and that you are using the correct fixture names in your test functions.
* **Parameterized Tests**: Leverage @pytest.mark.parametrize to run the same test function with multiple sets of inputs. This helps in validating different scenarios without duplicating code.
