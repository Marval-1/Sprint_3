class Locator:

    profile_button = "//a[@href='/account']" # Кнопка "Личный кабинет"
    auth_button_reg_under_auth_form = "//a[contains(text(), 'Зарегистрироваться')]" # Кнопка "Зарегистрироваться" под формой авторизации
    reg_input_name = "//label[contains(text(), 'Имя')]/following-sibling::input" # Поле ввода "Имя" в форме регистрации
    reg_input_email = "//label[contains(text(), 'Email')]/following-sibling::input" # Поле ввода "email" в форме регистрации
    reg_input_password = "//input[@name='Пароль']" # Поле ввода "Пароль" в форме регистрации
    reg_button_in_reg_form = "//button[contains(text(), 'Зарегистрироваться')]" # Кнопка "Зарегистироваться" в форме регистрации
    auth_header = "//h2[contains(text(), 'Вход')]" # Заголовок формы авторизации "Вход"
    reg_header = "//h2[contains(text(), 'Регистрация')]" # Заголовок формы авторизации "Регистрация"
    password_error_message = "//p[contains(text(), 'Некорректный пароль')]" # Сообщение об ошибке "Некорректный пароль"
    main_button_login = "//button[contains(text(), 'Войти в аккаунт')]" # Кнопка "Войти в аккаунт" на главной странице.
    auth_input_email = "//label[contains(text(), 'Email')]/following-sibling::input" # Поле ввода "email" в форме авторизации
    auth_input_password = "//input[@name='Пароль']" # Поле ввода "Пароль" в форме авторизации
    auth_button_in_auth_form = "//button[contains(text(), 'Войти')]" # Кнопка "Войти" в форме авторизации
    main_button_set_an_order = "//button[contains(text(), 'Оформить заказ')]" # Кнопка "Оформить заказ" на главной странице
    reg_button_login_under_reg_form = "//a[contains(text(), 'Войти')]" # Кнопка "Войти" под формой регистрации
    auth_button_password_recovery_under_auth_form = "//a[contains(text(), 'Восстановить пароль')]" # Кнопка "Восстановить пароль" под формой авторизации
    recovery_button_login = "//a[contains(text(), 'Войти')]" # Кнопка "Войти" под формой восстановления пароля
    account_button_exit = "//button[contains(text(), 'Выход')]" # Кнопка "Выход" в личном кабинете
    constructor_button = "//p[contains(text(), 'Конструктор')]" # Кнопка "Конструктор"
    main_header = "//h1[contains(text(), 'Соберите бургер')]" # Заголовок "Соберите бургер" на главной странице
    main_logo = "//div[@class='AppHeader_header__logo__2D0X2']" # Логотип Stellar Burgers на главной странице
    buns_button = "//span[contains(text(), 'Булки')]" # Кнопка "Булки"
    buns_header = "//h2[contains(text(), 'Булки')]" # Заголовок "Булки"
    sauce_button = "//span[contains(text(), 'Соусы')]" # Кнопка "Соусы"
    sauce_header = "//h2[contains(text(), 'Соусы')]" # Заголовок "Соусы"
    fillings_button = "//span[contains(text(), 'Начинки')]" # Кнопка "Начинки"
    fillings_header = "//h2[contains(text(), 'Начинки')]" # Заголовок "Начинки"
