from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти кликабельный элемент {locator}")
    def find_clickable_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = self.find_clickable_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def type_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Перейти по URL {url}")
    def go_to_url(self, url):
        self.driver.get(url)