from playwright.sync_api import Page, expect
import re


def test_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button").click()
    expect(page).to_have_url(re.compile("secure"))


def test_fill_in(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_placeholder("First Name").fill("Ivan")
    page.get_by_placeholder("Last Name").fill("Petrov")
    page.get_by_placeholder("name@example.com").fill("ivan@mail.com")
    page.locator('[for="gender-radio-1"]').check()
    page.get_by_placeholder("Mobile Number").fill("7891234567")
    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__year-select").select_option("1990")
    page.locator(".react-datepicker__month-select").select_option("0")
    page.locator(".react-datepicker__day--018").click()
    subject = page.locator("#subjectsInput")
    subject.fill("Maths")
    subject.press("Enter")
    page.get_by_text("Sports").click()
    page.get_by_placeholder("Current Address").fill("Moscow")
    state = page.locator("#react-select-3-input")
    state.fill("n")
    state.press("Enter")
    city = page.locator("#react-select-4-input")
    city.fill("d")
    city.press("Enter")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#example-modal-sizes-title-lg")).to_have_text(
        "Thanks for submitting the form"
    )
