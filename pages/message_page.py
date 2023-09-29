from playwright.sync_api import Page, expect

ADDRESSEE = "kofola-sp@azet.sk"

class MessagePage:

    def __init__(self, page: Page):
        self.page = page

    def check_if_message_dialog_exists(self):
        expect(self.page.get_by_label("Prijímateľ")).to_be_visible()

    def fill_addressee(self):
        self.page.get_by_label("Prijímateľ").click()
        self.page.get_by_label("Prijímateľ").fill(ADDRESSEE)

    def check_addressee_filled(self):
        expect(self.page.get_by_label("Prijímateľ")).to_have_value(ADDRESSEE)

    def fill_topic(self):
        self.page.get_by_label("Predmet").click()
        self.page.get_by_label("Predmet").fill("predmet")

    def check_topic_filled(self):
        expect(self.page.get_by_label("Predmet")).to_have_value("predmet")

    def fill_attachment(self):
        self.page.get_by_label("Vybrať prílohy").set_input_files("../resources/attachment.txt")

    def check_attachment_attached(self):
        expect(self.page.get_by_role("link", name="attachment.txt")).to_be_visible()

    def fill_mail_body(self):
        self.page.frame_locator("iframe[class='cke_wysiwyg_frame cke_reset']").locator("body").click()
        self.page.frame_locator("iframe[class='cke_wysiwyg_frame cke_reset']").locator("body").fill("gulas")

    def check_mail_body_filled(self):
        expect(self.page.frame_locator("iframe[class='cke_wysiwyg_frame cke_reset']").locator("body")).to_contain_text("gulas")

    def click_send_mail_button(self):
        self.page.wait_for_timeout(3000)
        self.page.locator("#teloSpravy").get_by_role("button", name="Odoslať").click()
        self.page.wait_for_timeout(3000)

    def check_if_mail_was_sent(self):
        self.page.get_by_role("link", name="Zobraziť správu").click()
        expect(self.page.get_by_text("gulas", exact=True)).to_have_text("gulas")