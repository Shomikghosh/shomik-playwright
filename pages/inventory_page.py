from playwright.sync_api import  expect
from pages.login_page import LoginPage

class InventoryPage:

    def __init__(self,page):
        self.inventory_list_selector = page.locator('[data-test="inventory-item"]')

        self.product_name_selector = page.locator('[data-test="inventory-item-name"]')
        self.product_description_selector = page.locator('[data-test="inventory-item-desc"]')
        self.product_item_price_selector = page.locator('[data-test="inventory-item-price"]')
        self.product_item_add_to_cart = page.get_by_role("button",name="Add to cart")

        self.product_filter_selector = page.locator('[data-test="product-sort-container"]')

    def login_to_inventory(self,page):
        login = LoginPage(page)
        login.navigate()

        login.login('standard_user','secret_sauce')

        login.validate_success()