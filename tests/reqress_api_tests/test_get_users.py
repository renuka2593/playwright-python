from playwright.sync_api import  APIRequestContext

def test_get_user_list(api_request_context: APIRequestContext):
    """Test to verify the retrieval of user list from the API."""
    response = api_request_context.get("/api/users/2")

    # Assert the response status code
    assert response.status == 200
    # Parse the JSON response
    response_json = response.json()

    # Verify the response structure contains 'data'
    assert "data" in response_json

    # Verify the specific user's email
    user_data = response_json["data"]
    assert "email" in user_data  # Check if 'email' key exists
    assert user_data["email"] == "janet.weaver@reqres.in"  # Assert the email value

    # Optionally, you can also verify other fields
    assert user_data["first_name"] == "Janet"
    assert user_data["last_name"] == "Weaver"
