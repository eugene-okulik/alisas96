import pytest
from playwright.sync_api import Page
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.search_page import SearchPage
from pages.desks_page import DesksPage


@pytest.fixture()
def product_page(page:Page):
    return ProductPage(page)


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def search_page(page):
    return SearchPage(page)


@pytest.fixture()
def desks_page(page):
    return DesksPage(page)


@pytest.fixture()
def add_item_to_cart(product_page):
    product_page.open_page()
    product_page.add_to_cart()
    product_page.check_cart_counter_equals_qty_of_items('1')


@pytest.fixture()
def opened_cart(cart_page):
    cart_page.open_page()


@pytest.fixture()
def opened_product(product_page):
    product_page.open_page()


@pytest.fixture()
def opened_desks(desks_page):
    desks_page.open_page()
