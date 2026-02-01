import re
from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", lambda alert: alert.accept())
    page.locator(".a-button").click()
    field = page.locator("#result-text")
    expect(field).to_have_text("Ok")


def test_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    new_page_link = page.locator("#new-page-button")
    with context.expect_page() as new_page_event:
        new_page_link.click()
    new_page = new_page_event.value
    result_text = new_page.locator("#result-text")
    expect(result_text).to_have_text("I am a new page in a new tab")
    expect(new_page_link).to_be_enabled()


def test_color_change_btn(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    color_btn = page.locator("#colorChange")
    expect(color_btn).to_have_class(re.compile("danger"))
    color_btn.click()
    visible_after_5_sec_btn = page.locator("#visibleAfter")
    expect(visible_after_5_sec_btn).to_be_visible()
