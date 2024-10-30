import pytest
import re
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("username, password, expected_title", [
    ("standard_user", "secret_sauce", "Swag Labs")
])
def test_login(page: Page, username, password, expected_title):
    page.goto("https://www.saucedemo.com/v1/")
    page.locator('#user-name').fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    expect(page).to_have_title(re.compile(expected_title))
