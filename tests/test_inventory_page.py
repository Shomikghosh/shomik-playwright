from playwright.sync_api import Page, expect
from pages.inventory_page import  InventoryPage


def test_verify_all_product_count(page: Page):
    
    inventoryPage = InventoryPage(page) 
    inventoryPage.login_to_inventory(page)

    expect(inventoryPage.inventory_list_selector).to_have_count(6)
    
