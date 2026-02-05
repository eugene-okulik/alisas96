from playwright.sync_api import Page, expect, Route
import json
from time import sleep


def test_catch_response(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        response_data = response.json()
        response_data["body"]["digitalMat"][0]["familyTypes"][0][
            "productName"
        ] = "яблокофон 17 про"
        response_data = json.dumps(response_data)
        route.fulfill(body=response_data)

    page.route("**/step0_iphone/**", handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.locator(
        """[data-trigger-click="click [data-relatedlink=':r8:_secondarybutton']"] > .rf-hcard-content-title"""
    ).click()
    product_name = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(product_name).to_have_text("яблокофон 17 про")
