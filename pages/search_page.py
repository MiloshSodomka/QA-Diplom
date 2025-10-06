from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class SearchPage(BasePage):
    # Locators
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-testid='product-card']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-testid='add-to-cart']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-testid='product-title']")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".no-results")

    @allure.step("Получить количество результатов поиска")
    def get_search_results_count(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS))

    @allure.step("Добавить товар в корзину по индексу {index}")
    def add_product_to_cart(self, index=0):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_buttons:
            add_buttons[index].click()
            return True
        return False

    @allure.step("Получить название товара по индексу {index}")
    def get_product_title(self, index=0):
        titles = self.driver.find_elements(*self.PRODUCT_TITLE)
        if titles:
            return titles[index].text
        return ""

    @allure.step("Проверить наличие сообщения 'Нет результатов'")
    def is_no_results_message_displayed(self):
        return self.is_element_visible(self.NO_RESULTS_MESSAGE)