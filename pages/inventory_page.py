from playwright.sync_api import  expect
from pages.login_page import LoginPage
import json

with open("test_data/products.json") as f:
    products_data = json.load(f)
    
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

    def filter_assertion(self,sort_type):

        for (i) in range(6):
            expect(self.product_name_selector.nth(i)).to_contain_text(products_data[sort_type][i]['name'])
            expect(self.product_description_selector.nth(i)).to_contain_text(products_data[sort_type][i]['description'])
            expect(self.product_item_price_selector.nth(i)).to_contain_text(products_data[sort_type][i]['price'])
            expect(self.product_item_add_to_cart.nth(i)).to_contain_text("Add to cart")