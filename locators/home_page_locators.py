from selenium.webdriver.common.by import By



class HomePageLocators:
    # кнопка "да все привыкли"
    ACCEPT_COOKIES_BUTTON = (By.ID, "rcc-confirm-button")
    # кнопка-логотип "Яндекс"
    YANDEX_LOGO_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    # кнопка-логотип "Самокат"
    SCOOTER_LOGO_BUTTON = (By.XPATH, "//img[@alt='Scooter']")
    # кнопка "Заказать" в шапке приложения
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    # кнопка "Заказать" в теле приложения(большая)
    ORDER_BUTTON_BIG = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    # изображение логотипа "Дзен" на dzen.ru
    DZEN_LOGO_HEADER = (By.XPATH, "//a[@data-testid='logo']")
    # кнопка вопроса в FAQ
    QUESTION_BUTTON = (By.XPATH, "//div[@id='accordion__heading-{}']")
    # поле ответа в FAQ
    ANSWER_FIELD = (By.XPATH, "//div[@id='accordion__panel-{}']")
    # последнее поле вопроса в FAQ
    LAST_QUESTION_BUTTON = (By.XPATH, "//div[@id='accordion__heading-7']")


