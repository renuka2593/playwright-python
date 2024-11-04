"""
Test suite for Adding products to cart.
"""
import pytest
from playwright.sync_api import Page, expect
from saucedemo_pages.page_manager import PageManager


@pytest.mark.parametrize("username, password, product_to_add, expected_url",
                         [
                             ("standard_user", "secret_sauce", "Sauce Labs Onesie",
                              "https://www.saucedemo.com/v1/inventory.html")
                         ])
def test_add_to_cart(page: Page, username, password, product_to_add, expected_url):
    page_manager = PageManager(page)
    page_manager.login_page.go_to()
    page_manager.login_page.login_as_standard_user(username, password)
    expect(page).to_have_url(expected_url)
    page_manager.inventory_page.add_item_to_cart(product_to_add)
    page_manager.inventory_page.go_to_cart()
    expect(page).to_have_url('https://www.saucedemo.com/v1/cart.html')
    page_manager.inventory_page.is_item_added_to_cart(product_to_add)
