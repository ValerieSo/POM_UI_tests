import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Вводим значение в поле "Имя"')
    def set_name(self, name):
        self.wait_and_find_element(OrderPageLocators.INPUT_NAME).send_keys(name)


    @allure. step('Вводим значение в поле "Фамилия"')
    def set_surname(self, surname):
        self.wait_and_find_element(OrderPageLocators.INPUT_SURNAME).send_keys(surname)


    @allure.step('Вводим значение в поле "Адрес:куда привезти самокат"')
    def set_address(self, address):
        self.wait_and_find_element(OrderPageLocators.INPUT_ADDRESS).send_keys(address)


    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self, metro):
        self.click_button(OrderPageLocators.INPUT_METRO)
        locator_formatted = self.format_locators(OrderPageLocators.INPUT_METRO_HINT, metro)
        self.scroll_to_element(locator_formatted)
        self.click_button(locator_formatted)

    @allure.step('Вводим значение в поле "Телефон: на него позвонит курьер')
    def set_phone_number(self, phone_number):
        self.wait_and_find_element(OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(phone_number)


    @allure.step('Кликаем на кнопку "Далее"')
    def click_next_button(self):
        self.click_button(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Выбираем дату доставки самоката')
    def choose_delivery_date(self, day):
        self.click_button(OrderPageLocators.INPUT_DATE)
        locator_formatted = self.format_locators(OrderPageLocators.INPUT_DATE_DAY, day)
        self.click_button(locator_formatted)

    @allure.step('Устанавливаем срок аренды')
    def choose_rental_period(self, period):
        self.click_button(OrderPageLocators.INPUT_RENTAL_PERIOD)
        locator_formatted = self.format_locators(OrderPageLocators.INPUT_RENTAL_PERIOD_HINT, period)
        self.click_button(locator_formatted)

    @allure.step('Выбираем цвет самоката')
    def choose_color(self, color):
        if color == 'black':
            self.click_button(OrderPageLocators.CHECKBOX_BLACK)
        elif color == 'grey':
            self.click_button(OrderPageLocators.CHECKBOX_GREY)

    @allure.step('Добавляем комментарий')
    def add_comment(self, comment):
        self.wait_and_find_element(OrderPageLocators.INPUT_COMMENT).send_keys(comment)


    @allure.step('Кликаем по кнопке "Заказать"')
    def click_finalize_order_button(self):
        self.click_button(OrderPageLocators.ORDER_BUTTON_ORDER_FORM)

    @allure.step('Соглашаемся с оформлением заказа')
    def confirm_order(self):
        self.click_button(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Получаем заголовок всплывающего окна с сообщением о результате создания заказа')
    def get_confirmation_text(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_SUCCESS_MESSAGE)

    @allure.step('Заполняем форму заказа')
    def set_order_scooter(self, order_info):
        self.set_name(order_info['name'])
        self.set_surname(order_info['surname'])
        self.set_address(order_info['address'])
        self.choose_metro_station(order_info['metro'])
        self.set_phone_number(order_info['phone_number'])
        self.click_next_button()
        self.choose_delivery_date(order_info['day'])
        self.choose_rental_period(order_info['period'])
        self.choose_color(order_info['color'])
        self.add_comment(order_info['comment'])
        self.click_finalize_order_button()
        self.confirm_order()

