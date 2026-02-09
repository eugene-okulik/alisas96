from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import product_page_locators as prod_loc


class ProductPage(BasePage):
    page_url = "shop/furn-9999-office-design-software-7"

    def add_to_cart(self):
        self.find(prod_loc.add_to_cart_button_loc).click()

    def open_cart(self):
        self.find(prod_loc.cart_loc).click()

    def get_item_name_text(self):
        return self.find(prod_loc.item_loc).text_content()

    def insert_qty_of_items(self, qty_of_items):
        qty_input = self.find(prod_loc.qty_input_loc)
        qty_input.clear()
        qty_input.fill(qty_of_items)

    def enter_item_name_in_search_string(self, item_name):
        search_string = self.find(prod_loc.search_string_loc)
        search_string.fill(item_name)
        search_string.press("Enter")
