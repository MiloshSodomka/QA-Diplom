from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class MainPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='поиск']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CART_BUTTON = (By.CSS_SELECTOR, "[data-testid='cart-button']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[data-testid='logout-button']")

    @allure.step("Выполнить поиск по запросу '{query}'")
    def search_for_product(self, query):
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.click(self.CART_BUTTON)

    @allure.step("Выйти из системы")
    def logout(self):
        self.click(self.LOGOUT_BUTTON)