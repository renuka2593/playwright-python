from saucedemo_pages.inventory_page import InventoryPage
from saucedemo_pages.login_page import LoginPage


class PageManager:
    """Manages page instances."""

    # Suppress too-few-public-methods warning
    # pylint: disable=too-few-public-methods
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
