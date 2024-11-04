from saucedemo_pages.login_page import LoginPage


class PageManager:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
