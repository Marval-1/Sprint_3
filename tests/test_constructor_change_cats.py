from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestConstructorNavigation:
    def test_constructor_move_to_fillings(self, driver):

        WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.fillings_button))).click()
        fillings = WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.fillings_header))).text

        assert fillings == "Начинки"

    def test_constructor_move_to_sauce(self, driver):

        WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.fillings_button))).click()
        WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.sauce_button))).click()
        sauce = WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.sauce_header))).text

        assert sauce == "Соусы"

    def test_constructor_move_to_buns(self, driver):

        WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.fillings_button))).click()
        WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.buns_button))).click()
        buns = WebDriverWait(driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.buns_header))).text

        assert buns == "Булки"
