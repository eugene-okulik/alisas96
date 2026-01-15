import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    driver.get("http://testshop.qa-practice.com/")
    desk = driver.find_element(By.CSS_SELECTOR, '[content="Customizable Desk"]')
    text = desk.text
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(desk)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "#add_to_cart")
    add_to_cart_button.click()
    time.sleep()
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-secondary")))
    continue_shopping = driver.find_element(By.CSS_SELECTOR, ".btn-secondary")
    continue_shopping.click()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(
        By.CSS_SELECTOR, "a.o_navlink_background .fa-shopping-cart.fa-stack"
    )
    cart.click()
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".d-inline")))
    product = driver.find_element(By.CSS_SELECTOR, ".d-inline")
    assert text in product.text
