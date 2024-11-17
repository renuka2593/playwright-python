import pytest
import json
import re
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture
def get_data(request):
    # Load the JSON file with test data
    with open('data/test_data.json', 'r') as file:
        data = json.load(file)

    # Get the name of the current test function being executed
    test_name = request.node.name
    base_test_name = re.sub(r'\[.*\]', '', test_name)
    # Return the relevant data based on the test name

    if base_test_name in data:
        return data[base_test_name][0]
    else:
        pytest.fail(f"No test data found for test function: {test_name}")

BASE_URL = "https://reqres.in"
HEADERS = {
    "Accept": "application/json"
}


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> APIRequestContext:
    """Fixture to create a new APIRequestContext with predefined headers and base URL."""
    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers=HEADERS,
    )
    yield request_context
    request_context.dispose()