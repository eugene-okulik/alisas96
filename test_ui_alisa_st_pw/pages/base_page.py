from playwright.sync_api import Page, Locator, expect
from pages.locators import desks_page_locators as desks_loc


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}{self.page_url}')

    def find(self, locator: Locator):
        return self.page.locator(locator)

    def move_to_elem(self, element: Locator):
        element.hover()

    def check_cart_counter_equals_qty_of_items(self, qty):
        cart_counter = self.find(desks_loc.cart_counter_loc)
        expect(cart_counter).to_have_text(qty)

