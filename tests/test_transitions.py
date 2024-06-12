import allure
from page_objects.home_page import HomePage
from data.data import Urls


class TestTransitions:
    @allure.title('Клик по кнопке "Самокат" в шапке ведет на главную страницу приложения')
    @allure.description('Переходим с главной страницы на страницу заказа, кликаем на кнопку "Самокат" в логотипе приложения в шапке приложения')
    def test_go_to_home_page_by_clicking_on_scooter_logo_header(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_button_header()
        home_page.click_scooter_logo()
        expected_url = Urls.BASE_URL
        actually_url = home_page.get_current_url()
        assert expected_url == actually_url, f'Ожидалась страница: "{expected_url}", получена "{actually_url}"'

    @allure.title('Клик по кнопке "Яндекс" в шапке ведет на главную страницу Дзена')
    @allure.description('Кликаем по кнопке "Яндекс" и переходим в новую вкладку')
    def test_go_to_dzen_by_clicking_on_yandex_logo_header(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_dzen_via_yandex_logo()
        home_page.wait_url_until_not_about_blank()
        actually_url = home_page.get_current_url()
        assert 'dzen.ru' in actually_url

