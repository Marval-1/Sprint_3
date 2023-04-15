import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from locators import Locator

url = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1200,1500")
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def login(driver):
    driver.find_element(By.XPATH, Locator.main_button_login).click()
    driver.find_element(By.XPATH, Locator.auth_input_email).send_keys("valentin_maruhin_8_777@gmail.com")
    driver.find_element(By.XPATH, Locator.auth_input_password).send_keys("123456")
    driver.find_element(By.XPATH, Locator.auth_button_in_auth_form).click()
    return driver
