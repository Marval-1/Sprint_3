from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from locators import Locator


class TestRegistration:
    def test_registration_correct(self, driver):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_reg_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.reg_input_name).send_keys("Валентин")
        driver.find_element(By.XPATH, Locator.reg_input_email).send_keys("valentin_maruhin_8_021@gmail.com")
        driver.find_element(By.XPATH, Locator.reg_input_password).send_keys("123456")
        driver.find_element(By.XPATH, Locator.reg_button_in_reg_form).click()
        time.sleep(3)
        reg = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.auth_header))).text

        assert reg == "Вход"

    def test_registration_without_name(self, driver):
        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_reg_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.reg_input_email).send_keys("valentin_maruhin_8_021@gmail.com")
        driver.find_element(By.XPATH, Locator.reg_input_password).send_keys("123456")
        driver.find_element(By.XPATH, Locator.reg_button_in_reg_form).click()
        time.sleep(3)
        reg = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.reg_header))).text

        assert reg == "Регистрация"

    def test_registration_with_incorrect_password(self,driver):
        driver.find_element(By.XPATH, Locator.profile_button).click()
        driver.find_element(By.XPATH, Locator.auth_button_reg_under_auth_form).click()
        driver.find_element(By.XPATH, Locator.reg_input_password).send_keys("123")
        driver.find_element(By.XPATH, Locator.reg_button_in_reg_form).click()
        time.sleep(3)
        reg = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.password_error_message))).text

        assert reg == "Некорректный пароль"
