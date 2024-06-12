import pytest
from data.data import Urls
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()
