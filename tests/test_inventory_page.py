from playwright.sync_api import Page, expect
from pages.inventory_page import  InventoryPage


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