from playwright.sync_api import Page, expect
import re


# def run(playwright: Playwright) -> None:
#     global browser
#     global context
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def check_if_loginform_is_available(self):
        self.page.get_by_placeholder("Zadaj názov účtu").click()

    def fill_out_username(self, username):
        self.page.get_by_placeholder("Zadaj názov účtu").click()
        self.page.get_by_placeholder("Zadaj názov účtu").fill(username)

    def fill_out_password(self, password):
        self.page.get_by_placeholder("Zadaj svoje heslo").click()
        self.page.get_by_placeholder("Zadaj svoje heslo").fill(password)

    def press_login_button(self):
        self.page.get_by_role("button", name="Prihlásiť sa").click()
