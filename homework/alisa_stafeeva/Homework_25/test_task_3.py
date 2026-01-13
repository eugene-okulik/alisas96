import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_choose_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select = driver.find_element(By.CSS_SELECTOR, "#id_choose_language")
    select_language = Select(select)
    select_language.select_by_value("1")
    text = select_language.first_selected_option.text
    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit-id-submit")
    submit_button.click()
    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#result-text")))
    result_text = driver.find_element(By.CSS_SELECTOR, "#result-text")
    assert result_text.text == text


def test_start_button(driver):
    text = "Hello World!"
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.CSS_SELECTOR, "#start > button")
    start_button.click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish > h4")))
    hello_world = driver.find_element(By.CSS_SELECTOR, "#finish > h4")
    assert hello_world.text == text
