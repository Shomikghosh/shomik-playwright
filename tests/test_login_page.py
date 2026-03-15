from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_login(page: Page):

    login = LoginPage(page)
    login.navigate()

    login.login('standard_user','secret_sauce')

    login.validate_success()

def test_invalid_login(page: Page):

    login = LoginPage(page)
    login.navigate()

    login.login('standard_use','secret_sauce')

    login.validate_error("Username and password do not match any user in this service")

def test_locked_login(page: Page):
    
    login=LoginPage(page)
    login.navigate()

    login.login('locked_out_user','secret_sauce')

    login.validate_error("Sorry, this user has been locked out.")

def test_empty_field_login(page: Page):
    
    login = LoginPage(page)
    login.navigate()

    login.login('','test_password')
    login.validate_error("Username is required")

    login.login('test_username','')
    login.validate_error("Password is required")
