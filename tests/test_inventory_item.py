from playwright.sync_api import Page, expect
from pages.inventory_item_page import  InventoryPageItem
import json

with open("test_data/products.json") as f:
    products_data = json.load(f)

def test_verify_inventory_item(page: Page):

    inventoryPageItem = InventoryPageItem(page) 
    inventoryPageItem.login_to_inventory(page)

    for (i) in range(6):
        inventoryPageItem.inventory_item_page_selector.nth(i).click()

        expect(inventoryPageItem.inventory_item_page_selector).to_contain_text(products_data['az'][i]['name'])
        expect(inventoryPageItem.inventory_item_desc_selector).to_contain_text(products_data['az'][i]['description'])
        expect(inventoryPageItem.inventory_item_price_selector).to_contain_text(products_data['az'][i]['price'])
        expect(inventoryPageItem.inventory_item_img_selector).to_have_attribute("alt",products_data['az'][i]['name'])

        inventoryPageItem.inventory_item_back_selector.click()





