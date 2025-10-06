import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.settings import settings
from api.client import ApiClient


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.BROWSER)
    parser.addoption("--headless", action="store", default=settings.HEADLESS)


@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    yield client


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(settings.TIMEOUT)
    driver.get(settings.BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.fixture
def search_page(driver):
    from pages.search_page import SearchPage
    return SearchPage(driver)


@pytest.fixture
def cart_page(driver):
    from pages.cart_page import CartPage
    return CartPage(driver)