class Locator:

    profile_button = "/html/body/div/div/header/nav/a" # Кнопка "Личный кабинет"
    auth_button_reg_under_auth_form = "/html/body/div/div/main/div/div/p[1]/a" # Кнопка "Зарегистрироваться" под формой авторизации
    reg_input_name = "/html/body/div/div/main/div/form/fieldset[1]/div/div/input" # Поле ввода "Имя" в форме регистрации
    reg_input_email = "/html/body/div/div/main/div/form/fieldset[2]/div/div/input" # Поле ввода "email" в форме регистрации
    reg_input_password = "/html/body/div/div/main/div/form/fieldset[3]/div/div/input" # Поле ввода "Пароль" в форме регистрации
    reg_button_in_reg_form = "/html/body/div/div/main/div/form/button" # Кнопка "Зарегистироваться" в форме регистрации
    auth_header = "/html/body/div/div/main/div/h2" # Заголовок формы авторизации "Вход"
    reg_header = "/html/body/div/div/main/div/h2" # Заголовок формы авторизации "Регистрация"
    password_error_message = "/html/body/div/div/main/div/form/fieldset[3]/div/p" # Сообщение об ошибке "Некорректный пароль"
    main_button_login = "/html/body/div/div/main/section[2]/div/button" # Кнопка "Войти в аккаунт" на главной странице.
    auth_input_email = "/html/body/div/div/main/div/form/fieldset[1]/div/div/input" # Поле ввода "email" в форме авторизации
    auth_input_password = "/html/body/div/div/main/div/form/fieldset[2]/div/div/input" # Поле ввода "Пароль" в форме авторизации
    auth_button_in_auth_form = "/html/body/div/div/main/div/form/button" # Кнопка "Войти" в форме авторизации
    main_button_set_an_order = "/html/body/div/div/main/section[2]/div/button" # Кнопка "Оформить заказ" на главной странице
    reg_button_login_under_reg_form = "/html/body/div/div/main/div/div/p/a" # Кнопка "Войти" под формой регистрации
    auth_button_password_recovery_under_auth_form = "/html/body/div/div/main/div/div/p[2]/a" # Кнопка "Восстановить пароль" под формой авторизации
    recovery_button_login = "/html/body/div/div/main/div/div/p/a" # Кнопка "Войти" под формой восстановления пароля
    account_button_exit = "/html/body/div/div/main/div/nav/ul/li[3]/button" # Кнопка "Выход" в личном кабинете
    constructor_button = "/html/body/div/div/header/nav/ul/li[1]/a/p" # Кнопка "Конструктор"
    main_header = "/html/body/div/div/main/section[1]/h1" # Заголовок "Соберите бургер" на главной странице
    main_logo = "/html/body/div/div/header/nav/div" # Логотип Stellar Burgers на главной странице
    buns_button = "/html/body/div/div/main/section[1]/div[1]/div[1]/span" # Кнопка "Булки"
    buns_header = "/html/body/div/div/main/section[1]/div[2]/h2[1]" # Заголовок "Булки"
    sauce_button = "/html/body/div/div/main/section[1]/div[1]/div[2]/span" # Кнопка "Соусы"
    sauce_header = "/html/body/div/div/main/section[1]/div[2]/h2[2]" # Заоловок "Соусы"
    fillings_button = "/html/body/div/div/main/section[1]/div[1]/div[3]/span" # Кнопка "Начинки"
    fillings_header = "/html/body/div/div/main/section[1]/div[2]/h2[3]" # Заголовок "Начинки"