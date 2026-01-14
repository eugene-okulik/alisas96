import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


def test_submit_text(driver):
    input_text = "Hello"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.CSS_SELECTOR, "#id_text_string")
    text_string.send_keys(input_text)
    text_string.submit()
    result_text = driver.find_element(By.CSS_SELECTOR, "#result-text")
    assert result_text.text == input_text
