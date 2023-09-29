import os

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.inbox_page import InboxPage
from pages.message_page import MessagePage

# CONSTANTS
EMAIL_HOME = "https://www.azet.sk/"


def sign_in(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()
    main_page.cookies_dialog_is_not_visible()
    main_page.click_login_button()
    login_page = LoginPage(page)
    login_page.check_if_loginform_is_available()
    login_page.fill_out_username(os.getenv('USERNAME'))
    login_page.fill_out_password(os.getenv('PASSWORD'))
    login_page.press_login_button()
    inbox_page = InboxPage(page)
    inbox_page.check_if_user_is_logged_in()


def go_to_send_mail(page):
    inbox_page = InboxPage(page)
    inbox_page.click_on_send_mail()
    message_page = MessagePage(page)
    message_page.check_if_message_dialog_exists()


def send_mail(page):
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_addressee()
    message_page.fill_topic()
    message_page.fill_mail_body()
    message_page.fill_attachment()
    message_page.click_send_mail_button()


def send_mail_and_check_it(page):
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_addressee()
    message_page.fill_topic()
    message_page.fill_mail_body()
    message_page.fill_attachment()
    message_page.click_send_mail_button()
    message_page.check_if_mail_was_sent()

def check_if_dropdownmenu_works(page):
    inbox_page = InboxPage(page)
    inbox_page = InboxPage(inbox_page.click_on_dropdown_menu())
    inbox_page.chech_if_dropdown_menu_present()

def log_out(page):
    inbox_page = InboxPage(page)
    inbox_page = InboxPage(inbox_page.click_on_dropdown_menu())
    inbox_page.click_sign_off_button()
    inbox_page.check_if_user_is_signed_off()