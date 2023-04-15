from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from locators import Locator


class TestMoveFromAccountToConstructor:
    def test_move_to_constructor_from_account_by_click_constructor(self, driver, login):
        time.sleep(1)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_button))).click()
        driver.find_element(By.XPATH, Locator.constructor_button).click()

        header = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.main_header))).text

        assert header == "Соберите бургер"

    def test_move_to_constructor_from_account_by_click_logo(self, driver, login):
        time.sleep(1)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_button))).click()
        driver.find_element(By.XPATH, Locator.main_logo).click()

        header = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.main_header))).text

        assert header == "Соберите бургер"
