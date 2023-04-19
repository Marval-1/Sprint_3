from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestLogout:
    def test_logout(self, driver, login):

        driver.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.account_button_exit))).click()

        logout = WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.auth_header))).text

        assert logout == "Вход"
