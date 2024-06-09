from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def should_be_visible(self, locator):
        return WebDriverWait(self.driver, 5).until_not(expected_conditions.visibility_of_element_located(locator))

    def should_not_be_visible(self, locator):
        return WebDriverWait(self.driver, 5).until_not(expected_conditions.visibility_of_element_located(locator))

    def click_button(self, locator):
        button = self.find_clickable_element(locator)
        button.click()


    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_text_from_element(self, locator):
        return self.wait_and_find_element(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(expected_conditions.url_to_be('about:blank'))
