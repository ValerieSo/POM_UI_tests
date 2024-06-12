from selenium.webdriver.common.by import By


class OrderPageLocators:
    # поле ввода "Имя"
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    # поле ввода "Фамилия"
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # поле ввода "Адрес: куда привезти заказ":
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # поле выбора станции метро
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # подсказка станции метро
    INPUT_METRO_HINT = (By.XPATH, "//div[text()='{}']/parent::button")
    # поле ввода номеора телефона
    INPUT_PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # кнопка "Далее" формы "Для кого самокат"
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    # поле выбора даты доставки самоката
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # день в выпадающем календаре
    INPUT_DATE_DAY = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--0{}']")
    # поле выбора срока аренды
    INPUT_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    # вариант срока аренды
    INPUT_RENTAL_PERIOD_HINT = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    # чекбокс "черный жемчуг"
    CHECKBOX_BLACK = (By.XPATH, "//input[@id ='black']")
    # чекбокс "серая безысходность"
    CHECKBOX_GREY = (By.XPATH, "//input[@id ='grey']")
    # поле ввода комментария
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # кнопка "Заказать" в форме заказа самоката
    ORDER_BUTTON_ORDER_FORM = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    # кнопка "Да" в окне поддтверждения заказа
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Да']")
    # заголовок всплывающего окна с сообщением о результате создания заказа
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal')]/div[text()='Заказ оформлен']")
