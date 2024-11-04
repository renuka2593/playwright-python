"""
Test suite for logging into Sauce Demo using Playwright.
"""
import re
import pytest
from playwright.sync_api import Page, expect
from saucedemo_pages.page_manager import PageManager


@pytest.mark.parametrize("username, password, expected_title", [
    ("standard_user", "secret_sauce", "Swag Labs")
])
def test_should_be_able_to_login(page: Page, username, password, expected_title):
    page_manager = PageManager(page)
    page_manager.login_page.go_to()
    page_manager.login_page.fill_username(username)
    page_manager.login_page.fill_password(password)
    page_manager.login_page.click_login()
    expect(page).to_have_title(re.compile(expected_title))


@pytest.mark.parametrize("username, password, expected_title", [
    ("locked_out_user", "secret_sauce", "Swag Labs")
])
def test_should_get_locked_error_msg(page: Page, username, password, expected_title):
    page_manager = PageManager(page)
    page_manager.login_page.go_to()
    page_manager.login_page.fill_username(username)
    page_manager.login_page.fill_password(password)
    page_manager.login_page.click_login()
    expect(page).to_have_title(re.compile(expected_title))
    expect(page_manager.login_page.get_error_msg()).to_contain_text("Sorry, this user has been locked out.")
