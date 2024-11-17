import pytest
import json
import re

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
