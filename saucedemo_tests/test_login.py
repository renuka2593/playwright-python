"""
Test suite for logging into Sauce Demo using Playwright.
"""
import re
import pytest
from playwright.sync_api import Page, expect
from saucedemo_pages.login_page import LoginPage


@pytest.mark.parametrize("username, password, expected_title", [
    ("standard_user", "secret_sauce", "Swag Labs")
])
def test_login(page: Page, username, password, expected_title):
    login_page = LoginPage(page)

    login_page.go_to()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.click_login()
    expect(page).to_have_title(re.compile(expected_title))
