from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator

name = "Валентин"
email = "valentin_maruhin_8_028@gmail.com"
password = "123456"
incorrect_pass = "123"


class TestRegistration:
    def test_registration_correct(self, driver):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_reg_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.reg_input_name).send_keys(name)
        driver.find_element(By.XPATH, Locator.reg_input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.reg_input_password).send_keys(password)
        driver.find_element(By.XPATH, Locator.reg_button_in_reg_form).click()

        reg = WebDriverWait(driver, 3)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.auth_header))).text

        assert reg == "Вход"

    def test_registration_without_name(self, driver):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_reg_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.reg_input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.reg_input_password).send_keys(password)
        driver.find_element(By.XPATH, Locator.reg_button_in_reg_form).click()

        reg = WebDriverWait(driver, 3)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.reg_header))).text

        assert reg == "Регистрация"

    def test_registration_with_incorrect_password(self, driver):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_reg_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.reg_input_password).send_keys(incorrect_pass)
        driver.find_element(By.XPATH, Locator.reg_button_in_reg_form).click()

        reg = WebDriverWait(driver, 3)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.password_error_message))).text

        assert reg == "Некорректный пароль"
