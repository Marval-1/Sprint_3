from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# -------------------------------Переход из личного кабинета в конструктор по клику на «Конструктор»
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

# Перехожу в личный кабинет по клику на "Личный кабинет"
# Нахожу кнопку "Личный кабинет" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу кнопку "Выход"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))

# Нахожу кнопку "Конструктор" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу заголовок "Соберите бургер"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))

driver.quit()

# -------------------------------Переход по из личного кабинета клику на логотип Stellar Burgers
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

# Перехожу в личный кабинет по клику на "Личный кабинет"
# Нахожу кнопку "Личный кабинет" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу кнопку "Выход"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))

# Нахожу логотип Stellar Burgers и кликаю по нему
driver.find_element(By.XPATH, '/html/body/div/div/header/nav/div/a').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу заголовок "Соберите бургер"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')))

driver.quit()
