from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# -------------------------------Без Имени
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

# Нахожу кнопку "Личный кабинет" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

# Нахожу кнопку "Зарегистрироваться" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

# Поле "Имя" оставляю пустым
# Ввожу email
# Ввожу Пароль

# Нахожу поле "Email" и заполняю его
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("valentin_maruhin_8_774@gmail.com")

# Нахожу поле "Пароль" и заполняю его
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys("123456")

# Нахожу кнопку "Зарегистрироваться" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Явное ожидание, пока. Убеждаюсь что перехода нет. Остаюсь в форме авторизации и вижу заголовок "Регистрация"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2')))


driver.quit()

# -------------------------------С Именем
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

# Нахожу кнопку "Личный кабинет" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

# Нахожу кнопку "Зарегистрироваться" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

# Нахожу поле "Имя" и заполняю его
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Валентин")

# Нахожу поле "Email" и заполняю его
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("valentin_maruhin_8_774@gmail.com")

# Нахожу поле "Пароль" и заполняю его
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys("123456")

# Нахожу кнопку "Зарегистрироваться" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Добавляю явное ожидание для загрузки страницы пока не увижу заголовок "Вход"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2')))

driver.quit()

# -------------------------------Ошибка некорректного пароля
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

# Нахожу кнопку "Личный кабинет" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

# Нахожу кнопку "Зарегистрироваться" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

# Нахожу поле "Пароль" и заполняю его
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys("123")

# Нахожу кнопку "Зарегистрироваться" и кликаю по ней
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div')))

driver.quit()
