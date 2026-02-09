import re
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import search_page_locators as search_loc


class SearchPage(BasePage):
	def check_requested_item_found(self, requested_text):
		item_found = self.find(search_loc.item_found_loc)
		expect(item_found).to_have_text(re.compile(requested_text))
