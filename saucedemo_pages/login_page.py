"""
Module containing the LoginPage class for the Sauce Demo application.
"""
from playwright.sync_api import Page


class LoginPage:
    """
    Page Object for the Sauce Demo login page.

    Attributes:
        page (Page): The Playwright Page object to interact with the browser.
        username_locator (str): The locator for the username input field.
        password_locator (str): The locator for the password input field.
        login_button_locator (str): The locator for the login button.
    """

    def __init__(self, page: Page):
        self.page = page
        self.username_locator = '#user-name'
        self.password_locator = '#password'
        self.login_button_locator = '#login-button'
        self.error_msg_txt = "Sorry, this user has been locked out."

    def go_to(self):
        self.page.goto("https://www.saucedemo.com/v1/")

    def fill_username(self, username: str):
        self.page.locator(self.username_locator).fill(username)

    def fill_password(self, password: str):
        self.page.locator(self.password_locator).fill(password)

    def click_login(self):
        self.page.locator(self.login_button_locator).click()

    def get_error_msg(self):
        return self.page.get_by_text(self.error_msg_txt)
