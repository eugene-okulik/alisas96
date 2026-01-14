import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_fill_the_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    first_name = driver.find_element(By.CSS_SELECTOR, "#firstName")
    first_name.send_keys("Svetlana")
    last_name = driver.find_element(By.CSS_SELECTOR, "#lastName")
    last_name.send_keys("Petrova")
    email = driver.find_element(By.CSS_SELECTOR, "#userEmail")
    email.send_keys("jkgdvsjklcnb@gmail.ru")
    gender = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-2"]')
    gender.click()
    mobile_number = driver.find_element(By.CSS_SELECTOR, "#userNumber")
    mobile_number.send_keys("1234567890")
    date_of_birth = driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput")
    date_of_birth.click()
    select_year = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
    year = Select(select_year)
    year.select_by_value("1996")
    select_month = driver.find_element(
        By.CSS_SELECTOR, ".react-datepicker__month-select"
    )
    month = Select(select_month)
    month.select_by_value("11")
    day = driver.find_element(
        By.CSS_SELECTOR, '[aria-label="Choose Tuesday, December 10th, 1996"]'
    )
    day.click()
    time.sleep(3)
    subjects_menu = driver.find_element(By.CSS_SELECTOR, "#subjectsInput")
    subjects_menu.send_keys("Maths")
    subjects_menu.send_keys(Keys.ENTER)
    hobbies = driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-1"]')
    hobbies.click()
    scroll = driver.find_element(By.CSS_SELECTOR, "body")
    scroll.send_keys(Keys.PAGE_DOWN)
    address = driver.find_element(By.CSS_SELECTOR, "#currentAddress")
    address.send_keys("Baker street")
    state = driver.find_element(By.CSS_SELECTOR, "#react-select-3-input")
    state.send_keys("n")
    state.send_keys(Keys.ENTER)
    city = driver.find_element(By.CSS_SELECTOR, "#react-select-4-input")
    city.send_keys("d")
    city.send_keys(Keys.ENTER)
    submit = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit.click()
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
        )
    )
    form_is_submitted = driver.find_element(
        By.CSS_SELECTOR, "#example-modal-sizes-title-lg"
    )
    text = "Thanks for submitting the form"
    assert form_is_submitted.text == text
    print(form_is_submitted.text)
