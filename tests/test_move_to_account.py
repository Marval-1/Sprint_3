from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from locators import Locator


class TestMoveToAccount:
    def test_move_to_account(self, driver, login):
        time.sleep(1)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_button))).click()

        nav = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.account_button_exit))).text

        assert nav == "Выход"
