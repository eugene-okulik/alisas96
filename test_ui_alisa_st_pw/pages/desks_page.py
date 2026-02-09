from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import desks_page_locators as desks_loc
from pages.locators import desks_page_locators as prod_loc


class DesksPage(BasePage):
    page_url = "shop/category/desks-1"

    def items(self):
        return self.find(desks_loc.desks_loc)

    def prices(self):
        return self.find(desks_loc.prices_loc)

    def check_items_displayed(self):
        expect(self.items().first).to_be_visible()

    def check_all_items_have_price(self):
        expect(self.items()).to_have_count(self.prices().count())

    def check_all_items_have_img(self):
        expect(self.items()).to_have_count(self.find(desks_loc.imgs_loc).count())

    def sort_by_price_low_to_high(self):
        sort_by_button = self.find(desks_loc.sort_by_button_loc)
        sort_by_button.click()
        sort_by_price = self.find(desks_loc.sort_by_price_loc)
        sort_by_price.click()

    def check_sorted_by_price_low_to_high(self):
        price_list = [
            float(price.replace(",", "")) for price in self.prices().all_text_contents()
        ]
        assert sorted(price_list) == price_list

    def add_desk_to_cart(self):
        first_desk = self.find(desks_loc.desks_loc).first
        self.move_to_elem(first_desk)
        add_desk = self.find(desks_loc.add_desk_button_loc).first
        add_desk.click()
        continue_button = self.find(desks_loc.continue_button_loc)
        continue_button.click()
