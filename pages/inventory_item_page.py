from pages.login_page import LoginPage

class InventoryPageItem:

    def __init__(self,page):
        
        self.inventory_item_page_selector = page.locator('[data-test="inventory-item-name"]')
        self.inventory_item_desc_selector = page.locator('[data-test="inventory-item-desc"]')
        self.inventory_item_price_selector = page.locator('[data-test="inventory-item-price"]')
        self.inventory_item_img_selector = page.locator('.inventory_details_img')
        self.inventory_item_back_selector = page.locator('[data-test="back-to-products"]')

    def login_to_inventory(self,page):
        login = LoginPage(page)
        login.navigate()

        login.login('standard_user','secret_sauce')

        login.validate_success()