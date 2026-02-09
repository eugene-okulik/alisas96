import re
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import cart_page_locators as cart_loc


class CartPage(BasePage):
    page_url = "shop/cart"

    def check_chosen_item_in_cart(self, requested_text):
        item_in_cart = self.find(cart_loc.item_in_cart_loc)
        expect(item_in_cart).to_have_text(re.compile(requested_text))

    def remove_item_from_cart(self):
        remove_button = self.find(cart_loc.item_in_cart_loc)
        remove_button.click()

    def check_cart_is_empty(self):
        items = self.find(cart_loc.item_in_cart_loc)
        expect(items).to_have_count(0)

    def check_cart_is_not_empty(self):
        items = self.find(cart_loc.item_in_cart_loc)
        expect(items.first).to_be_visible()

    def go_to_checkout(self):
        checkout_button = self.find(cart_loc.checkout_button_loc)
        checkout_button.click()

    def check_there_is_a_shipping_form(self):
        expect(self.page).to_have_url(re.compile("address"))
