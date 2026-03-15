from playwright.sync_api import  expect

class LoginPage:

    def __init__(self,page):
        self.page = page
        self.username = page.get_by_placeholder('Username')
        self.password = page.get_by_placeholder('Password')
        self.login_button = page.get_by_role("button", name="Login")

        self.error_message = page.locator('[data-test="error"]')
        self.validate_success_locator = page.locator('[data-test="title"]')
        self.validate_inventory_content_locator = page.locator('[data-test="inventory-container"]')

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self,usr,password):
        self.username.fill(usr)
        self.password.fill(password)
        self.login_button.click()

    def validate_success(self):
        expect(self.validate_success_locator).to_be_visible()
        expect(self.validate_inventory_content_locator).to_be_visible()

    def validate_error(self,msg):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(msg)
