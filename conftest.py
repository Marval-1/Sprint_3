import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator

url = "https://stellarburgers.nomoreparties.site/"
email = "valentin_maruhin_8_777@gmail.com"
password = "123456"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,1500")
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(By.XPATH, Locator.main_button_login).click()
    driver.find_element(By.XPATH, Locator.auth_input_email).send_keys(email)
    driver.find_element(By.XPATH, Locator.auth_input_password).send_keys(password)
    driver.find_element(By.XPATH, Locator.auth_button_in_auth_form).click()
    WebDriverWait(driver, 10)\
        .until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.profile_button)))
    return driver
