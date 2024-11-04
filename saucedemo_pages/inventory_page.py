from playwright.sync_api import Page, expect


class InventoryPage:
    """Manages the inventory page actions."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_link = self.page.locator('a.shopping_cart_link')
        self.inventory_item_name = self.page.locator('.inventory_item_name')

    def go_to_cart(self):
        """Navigate to the shopping cart."""
        self.cart_link.click()

    def add_item_to_cart(self, item: str):
        """Add a specified item to the cart."""
        item_locator = self.page.locator('.inventory_item').filter(has_text=item)
        item_locator.get_by_role('button', name='ADD TO CART').click()

    def is_item_added_to_cart(self, item: str):
        """Check if the specified item is added to the cart."""
        item_locator = self.inventory_item_name.filter(has_text=item)
        expect(item_locator).to_have_count(1)
