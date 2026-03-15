from playwright.sync_api import Page, expect
from pages.inventory_page import  InventoryPage
import json

with open("test_data/products.json") as f:
    products_data = json.load(f)

def test_verify_all_product_count(page: Page):
    
    inventoryPage = InventoryPage(page) 
    inventoryPage.login_to_inventory(page)

    expect(inventoryPage.inventory_list_selector).to_have_count(6)
    
def test_verify_all_inventory_content(page: Page):

    inventoryPage = InventoryPage(page) 
    inventoryPage.login_to_inventory(page)

    for (i) in range(6):
        expect(inventoryPage.product_name_selector.nth(i)).to_be_visible()
        expect(inventoryPage.product_description_selector.nth(i)).to_be_visible()
        expect(inventoryPage.product_item_price_selector.nth(i)).to_be_visible()
        expect(inventoryPage.product_item_add_to_cart.nth(i)).to_be_visible()

def test_sort_a_to_z_sort(page: Page):

    inventoryPage = InventoryPage(page)
    inventoryPage.login_to_inventory(page)

    for (i) in range(6):
            expect(inventoryPage.product_name_selector.nth(i)).to_contain_text(products_data['az'][i]['name'])
            expect(inventoryPage.product_description_selector.nth(i)).to_contain_text(products_data['az'][i]['description'])
            expect(inventoryPage.product_item_price_selector.nth(i)).to_contain_text(products_data['az'][i]['price'])
            expect(inventoryPage.product_item_add_to_cart.nth(i)).to_contain_text("Add to cart")

def test_sort_z_to_a_sort(page: Page):

    inventoryPage = InventoryPage(page)
    inventoryPage.login_to_inventory(page)

    inventoryPage.product_filter_selector.select_option('Name (Z to A)')


    for (i) in range(6):
            expect(inventoryPage.product_name_selector.nth(i)).to_contain_text(products_data['za'][i]['name'])
            expect(inventoryPage.product_description_selector.nth(i)).to_contain_text(products_data['za'][i]['description'])
            expect(inventoryPage.product_item_price_selector.nth(i)).to_contain_text(products_data['za'][i]['price'])
            expect(inventoryPage.product_item_add_to_cart.nth(i)).to_contain_text("Add to cart")
