import os

from pytest_bdd import scenario, given, when, then
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.inbox_page import InboxPage
from pages.message_page import MessagePage

from workflows import email_workflow as EmailWorkflow

# CONSTANTS
EMAIL_HOME = "https://www.azet.sk/"


@scenario('email.feature', 'Login into the gmail')
def publish():
    assert True


@given("I am already registered to the email website")
def test_step_impl1():
    assert True


@given("I am on the login page")
def test_goto_login_page(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)


##################### COOKIES
@given("Cookies dialog pops up")
def test_cookies_dialog_present(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.cookies_dialog_is_visible()


@when("I have accepted cookies")
def test_accept_cookies(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()


@then("Cookies dialog closes")
def test_cookies_dialog_closes(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()
    main_page.cookies_dialog_is_not_visible()


##################### LOGIN

@when("I have clicked login button")
def test_click_login_button(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()
    main_page.cookies_dialog_is_not_visible()
    main_page.click_login_button()


@then("I should be redirected to login page")
def test_redirected_to_login_page(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()
    main_page.cookies_dialog_is_not_visible()
    main_page.click_login_button()
    login_page = LoginPage(page)
    login_page.check_if_loginform_is_available()


@when('I have entered <username> into "username" field')
def test_enter_username(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()
    main_page.cookies_dialog_is_not_visible()
    main_page.click_login_button()
    login_page = LoginPage(page)
    login_page.check_if_loginform_is_available()
    login_page.fill_out_username(os.getenv('USERNAME'))


@when('I have entered <password> into "password" field')
def test_enter_password(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()
    main_page.cookies_dialog_is_not_visible()
    main_page.click_login_button()
    login_page = LoginPage(page)
    login_page.check_if_loginform_is_available()
    login_page.fill_out_username(os.getenv('USERNAME'))
    login_page.fill_out_password(os.getenv('PASSWORD'))


@when('I pressed the "log in" button')
def test_login(page):
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


@then("I should be logged in and redirected to my email inbox")
def test_login_successfull(page):
    main_page = MainPage(page)
    main_page.go_to_email_homepage(EMAIL_HOME)
    main_page.accept_cookies()
    main_page.cookies_dialog_is_not_visible()
    main_page.click_login_button()
    login_page = LoginPage(page)
    login_page.check_if_loginform_is_available()
    login_page.fill_out_username(os.getenv('username'))
    login_page.fill_out_password(os.getenv('password'))
    login_page.press_login_button()
    inbox_page = InboxPage(page)
    inbox_page.check_if_user_is_logged_in()


@scenario('email.feature', 'Creating and sending email to addressee from contacts with file attachment')
def publish2():
    pass


@given("I am logged in and I'm in my inbox")
def test_logged_in_inbox(page):
    EmailWorkflow.sign_in(page)


@when('I click on "write e-mail" button')
def test_write_email_button(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    inbox_page.click_on_send_mail()


@then("Window with email form is opened")
def test_email_form_opens(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.check_if_message_dialog_exists()


@when("I fill out addressee of mail")
def test_fill_addressee(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_addressee()


@then("addressee of mail should be filled out")
def test_fill_addressee_check(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_addressee()
    message_page.check_addressee_filled()


@when("I fill out topic of mail")
def test_fill_topic(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_topic()

@then("topic of mail should be filled out")
def test_fill_topic_check(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_topic()
    message_page.check_topic_filled()


@when("I fill out body of mail")
def test_fill_body(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_mail_body()


@then("body of mail should be filled out")
def test_fill_body_check(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_mail_body()
    message_page.check_mail_body_filled()


@when("I attach a file")
def test_attach_file(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_attachment()


@then("file should be attached")
def test_attach_file_check(page):
    EmailWorkflow.sign_in(page)
    inbox_page = InboxPage(page)
    message_page = MessagePage(inbox_page.click_on_send_mail())
    message_page.fill_attachment()
    message_page.check_attachment_attached()


@when("I click on send email")
def test_send_email(page):
    EmailWorkflow.sign_in(page)
    EmailWorkflow.send_mail(page)

@then("Mail should be sent to addressee")
def test_mail_should_be_sent(page):
    EmailWorkflow.sign_in(page)
    EmailWorkflow.send_mail_and_check_it(page)


@scenario('email.feature', 'Log out from the email')
def publish():
    pass


@given("I am logged in into the system")
@when("I click my avatar in top right corner")
@then("Drop-down menu is opened")
def test_dropdown_menu(page):
    EmailWorkflow.sign_in(page)
    EmailWorkflow.check_if_dropdownmenu_works(page)


@when("I click log out")
@then("I should be logged out from email")
def test_logout(page):
    EmailWorkflow.sign_in(page)
    EmailWorkflow.log_out(page)
