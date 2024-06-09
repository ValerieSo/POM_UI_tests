import allure
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage
from data.data import generate_order_info


class TestOrderPage:
    @allure.title('Позитивная проверка заказа самоката через кнопку "Заказать" в шапке приложения')
    @allure.description('Принимаем куки, нажимаем на кнопку"Заказать" в шапке приложения, заполняем поля формы "Для кого самокат", '
                        'заполняем поля формы " Про аренду", нажимаем кнопку "Заказать", в открывшемся окне поддтверждения заказа нажимаем кнопку "Да", '
                        'получаем визуальное подтверждение, что заказ оформлен')
    def test_order_scooter_by_clicking_order_button_header(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_info = generate_order_info()
        order_page.set_order_scooter(order_info)
        expected_message = order_page.get_confirmation_text()
        assert 'Заказ оформлен' in expected_message

    @allure.title('Позитивная проверка заказа самоката через кнопку "Заказать" в теле приложения')
    @allure.description('Принимаем куки, прокручиваем страницу до кнопки "Заказать" в разделе "Как это работает" и нажимаем на нее, '
                        'заполняем поля формы "Для кого самокат", заполняем поля формы " Про аренду", нажимаем кнопку "Заказать", '
                        'в открывшемся окне поддтверждения заказа нажимаем кнопку "Да", получаем визуальное подтверждение, что заказ оформлен')
    def test_order_scooter_by_clicking_order_button_body(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_order_button_body()
        order_page = OrderPage(driver)
        order_info = generate_order_info()
        order_page.set_order_scooter(order_info)
        expected_message = order_page.get_confirmation_text()
        assert 'Заказ оформлен' in expected_message





