import pytest
from playwright.async_api import Page


@pytest.mark.parametrize("username, password, expected_url", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/v1/inventory.html")
])
def test_login(page: Page, username, password, expected_url):
    page.goto("https://www.saucedemo.com/v1/")
    page.locator('#user-name').fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    assert page.url == expected_url, "Login failed or URL did not match expected dashboard URL"
