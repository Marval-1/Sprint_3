from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator

email = "valentin_maruhin_8_777@gmail.com"
password = "123456"


class TestLogin:
    def test_login_from_main_page(self, driver):

        driver.find_element(By.XPATH, Locator.main_button_login).click()
        driver.find_element(By.XPATH, Locator.auth_input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.auth_input_password).send_keys(password)
        driver.find_element(By.XPATH, Locator.auth_button_in_auth_form).click()

        auth = WebDriverWait(driver, 3)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.main_button_set_an_order))).text

        assert auth == "Оформить заказ"

    def test_login_from_profile(self, driver):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.auth_input_password).send_keys(password)
        driver.find_element(By.XPATH, Locator.auth_button_in_auth_form).click()

        auth = WebDriverWait(driver, 3)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.main_button_set_an_order))).text

        assert auth == "Оформить заказ"

    def test_login_from_registration(self, driver):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_reg_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.reg_button_login_under_reg_form).click()
        driver.find_element(By.XPATH, Locator.auth_input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.auth_input_password).send_keys(password)
        driver.find_element(By.XPATH, Locator.auth_button_in_auth_form).click()

        auth = WebDriverWait(driver, 3)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.main_button_set_an_order))).text

        assert auth == "Оформить заказ"

    def test_login_from_password_recovery(self, driver):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_password_recovery_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.recovery_button_login).click()
        driver.find_element(By.XPATH, Locator.auth_input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.auth_input_password).send_keys(password)
        driver.find_element(By.XPATH, Locator.auth_button_in_auth_form).click()

        auth = WebDriverWait(driver, 3)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.main_button_set_an_order))).text

        assert auth == "Оформить заказ"
