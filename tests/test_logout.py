from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Вход по кнопке «Войти в аккаунт» на главной
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

# Нахожу кнопку "Войти в аккаунт" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Нахожу поле "Email" и заполняю его
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("valentin_maruhin_8_777@gmail.com")

# Нахожу поле "Пароль" и заполняю его
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("123456")

# Нахожу кнопку "Войти" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу кнопку Оформить заказ
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

# Нахожу кнопку "Личный кабинет" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу кнопку "Выход"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))

# Нахожу кнопку "Выход" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу заголовок "Вход"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2')))

driver.quit()
