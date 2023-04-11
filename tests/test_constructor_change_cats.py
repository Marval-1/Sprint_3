from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

# Нахожу кнопку "Войти в аккаунт" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Нахожу поле "Email" и заполняю его
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("valentin_maruhin_8_777@gmail.com")

# Нахожу поле "Пароль" и заполняю его
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("123456")

# Нахожу кнопку "Войти" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу кнопку Оформить заказ
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

# Нахожу раздел "Начинки" и кликаю по нему
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()

# Добавляю явное ожидание для загрузки списка пока не увижу заголовок "Начинки"
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')))

# Нахожу раздел "Соусы" и кликаю по нему
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()

# Добавляю явное ожидание для загрузки списка пока не увижу заголовок "Соусы"
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]')))

# Нахожу раздел "Булки" и кликаю по нему
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()

# Добавляю явное ожидание для загрузки списка пока не увижу заголовок "Булки"
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')))

driver.quit()
