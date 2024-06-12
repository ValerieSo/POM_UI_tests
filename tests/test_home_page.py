import pytest
import allure
from page_objects.home_page import HomePage
from data.data import FaqAnswers


class TestHomePage:
    @allure.title('Проверка соответствия вопросов и ответов в разделе "Вопросы о важном" на главной странице')
    @allure.description('Соглашаемся с политикой насчет куков, скроллим главную страницу вниз до последнего вопроса, кликаем по каждому вопросу, проверяем, что ответ на вопрос соответствует ожидаемым значениям, определенным в FaqAnswers, по порядковому номеру вопроса (num).')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, FaqAnswers.ANSWER_0),
            (1, FaqAnswers.ANSWER_1),
            (2, FaqAnswers.ANSWER_2),
            (3, FaqAnswers.ANSWER_3),
            (4, FaqAnswers.ANSWER_4),
            (5, FaqAnswers.ANSWER_5),
            (6, FaqAnswers.ANSWER_6),
            (7, FaqAnswers.ANSWER_7)
        ]
    )
    def test_check_answer_matches_question(self, driver, num, result):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        expected_answer = result
        actually_answer = home_page.get_text_answer_faq(num)
        assert actually_answer == expected_answer, f'Ожидался ответ: "{expected_answer}", получено "{actually_answer}"'
