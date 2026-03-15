from playwright.sync_api import  expect
from pages.login_page import LoginPage

class InventoryPage:

    def __init__(self,page):
        self.inventory_list_selector = page.locator('[data-test="inventory-item"]')

    def login_to_inventory(self,page):
        login = LoginPage(page)
        login.navigate()

        login.login('standard_user','secret_sauce')

        login.validate_success()