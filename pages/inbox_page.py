import os

from playwright.sync_api import Page, expect


class InboxPage:

    def __init__(self, page: Page):
        self.page = page

    def check_if_user_is_logged_in(self):
        with self.page.expect_popup() as page_info:
            self.page.locator("span").filter(has_text="E-mail").click()
        inbox_page = page_info.value
        expect(inbox_page.get_by_title("Azet.sk", exact=True)).to_be_visible()


    def click_on_send_mail(self):
        with self.page.expect_popup() as page_info:
            self.page.locator("span").filter(has_text="E-mail").click()
        inbox_page = page_info.value
        expect(inbox_page.get_by_title("Azet.sk", exact=True)).to_be_visible()
        inbox_page.get_by_role("link", name="n Písať nový mail").click()
        return inbox_page



    def check_if_mail_was_sent(self):
        self.page.get_by_role("link", name="Zobraziť správu").click()
        expect(self.page.get_by_text("gulas", exact=True)).to_have_text("gulas")


    def chech_if_dropdown_menu_present(self):
        expect(self.page.get_by_role("link", name="Odhlásiť")).to_be_visible()
        expect(self.page.get_by_role("link", name="Email", exact=True)).to_be_visible()


    def click_sign_off_button(self):
        self.page.get_by_role("link", name="Odhlásiť").click()


    def check_if_user_is_signed_off(self):
        expect(self.page.get_by_role("link", name="Azet logo")).to_be_visible()


    def click_on_dropdown_menu(self):
        with self.page.expect_popup() as page_info:
            self.page.locator("span").filter(has_text="E-mail").click()
        inbox_page = page_info.value
        expect(inbox_page.get_by_title("Azet.sk", exact=True)).to_be_visible()
        inbox_page.locator("#ab_showmenu").click()
        return inbox_page