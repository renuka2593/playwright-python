from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_locator = '#user-name'
        self.password_locator = '#password'
        self.login_button_locator = '#login-button'

    def go_to(self):
        self.page.goto("https://www.saucedemo.com/v1/")

    def fill_username(self, username: str):
        self.page.locator(self.username_locator).fill(username)

    def fill_password(self, password: str):
        self.page.locator(self.password_locator).fill(password)

    def click_login(self):
        self.page.locator(self.login_button_locator).click()

