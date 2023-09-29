from playwright.sync_api import Page, expect
import re
# def run(playwright: Playwright) -> None:
#     global browser
#     global context
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()

class MainPage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_email_homepage(self, destination):
        self.page.goto(destination)

    def cookies_dialog_is_visible(self):
        expect(self.page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Prijať všetko")).to_be_visible()

    def cookies_dialog_is_not_visible(self):
        expect(self.page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Prijať všetko")).not_to_be_visible()

    def accept_cookies(self):
        self.page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Prijať všetko").click()

    def click_login_button(self):
        self.page.locator("span").filter(has_text=re.compile(r"^E-mail$")).click()

    def check_if_user_is_logged_in(self):
        with self.page.expect_popup() as page_info:
            self.page.locator("span").filter(has_text="E-mail").click()
        inbox_page = page_info.value
        expect(inbox_page.get_by_title("Azet.sk", exact=True)).to_be_visible()
        return inbox_page

    # with sync_playwright() as playwright:
    #     run(playwright)
    #     go_to_email_homepage("https://www.azet.sk/")
    #     # cookies_dialog_is_visible()
    #     # accept_cookies()
    #     # cookies_dialog_is_not_visible()
    #     # fill_out_username()
    #     # fill_out_password()
    #     # press_login_button()
    #     # check_if_user_is_logged_in()
    #     # page1.wait_for_timeout(3000)
    #     # send_mail_with_attachment()
    #     # check_if_mail_was_sent()
    #     # page1.wait_for_timeout(3000)
    #     # close_env()
