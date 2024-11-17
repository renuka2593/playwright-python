"""
Test suite for Adding products to cart.
"""
import pytest
from playwright.sync_api import Page, expect
from saucedemo_pages.page_manager import PageManager


def test_add_to_cart(page: Page, get_data):
    page_manager = PageManager(page)
    page_manager.login_page.go_to()
    page_manager.login_page.login_as_standard_user(get_data['username'], get_data['password'])
    expect(page).to_have_url(get_data['expected_url'])
    page_manager.inventory_page.add_item_to_cart(get_data['product_to_add'])
    page_manager.inventory_page.go_to_cart()
    expect(page).to_have_url('https://www.saucedemo.com/v1/cart.html')
    page_manager.inventory_page.is_item_added_to_cart(get_data['product_to_add'])
