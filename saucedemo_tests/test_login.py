from playwright.sync_api import sync_playwright, Playwright


def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/v1/")
    page.locator('#user-name').fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    assert page.url == "https://www.saucedemo.com/v1/inventory.html", "Login failed or URL did not match expected dashboard URL"


with sync_playwright() as playwright:
    test_login(playwright)
