import allure
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Отключаем перекрывающее контент сообщение о принятии куков')
    def accept_cookies(self):
        self.click_button(HomePageLocators.ACCEPT_COOKIES_BUTTON)
        self.should_not_be_visible(HomePageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Кликаем по кнопке "Яндекс" в шапке')
    def click_yandex_logo(self):
        self.click_button(HomePageLocators.YANDEX_LOGO_BUTTON)

    @allure.step('Переходим во вкладку Дзен')
    def go_to_dzen_via_yandex_logo(self):
        self.click_yandex_logo()
        self.switch_to_new_window()
        self.should_be_visible(HomePageLocators.DZEN_LOGO_HEADER)

    @allure.step('Кликаем по кнопке "Самокат" в шапке')
    def click_scooter_logo(self):
        self.click_button(HomePageLocators.SCOOTER_LOGO_BUTTON)


    @allure.step('Кликаем по кнопке "Заказать" в шапке')
    def click_order_button_header(self):
        self.click_button(HomePageLocators.ORDER_BUTTON_HEADER)


    @allure.step('Кликаем по кнопке "Заказать" в теле приложения')
    def click_order_button_body(self):
        self.scroll_to_element(HomePageLocators.ORDER_BUTTON_BIG)
        self.click_button(HomePageLocators.ORDER_BUTTON_BIG)

    @allure.step('Скроллим вниз и кликаем на кнопку вопроса в FAQ')
    def click_question_faq(self, num):
        self.scroll_to_element(HomePageLocators.LAST_QUESTION_BUTTON)
        locator_q_formatted = self.format_locators(HomePageLocators.QUESTION_BUTTON, num)
        self.click_button(locator_q_formatted)

    @allure.step('Получаем текст ответа')
    def get_text_answer_faq(self, num):
        self.click_question_faq(num)
        locator_a_formatted = self.format_locators(HomePageLocators.ANSWER_FIELD, num)
        return self.get_text_from_element(locator_a_formatted)
