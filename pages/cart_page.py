from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, "[data-testid='cart-item']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-testid='remove-from-cart']")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".empty-cart")
    TOTAL_PRICE = (By.CSS_SELECTOR, "[data-testid='total-price']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-testid='checkout-button']")

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    @allure.step("Удалить товар из корзины по индексу {index}")
    def remove_item_from_cart(self, index=0):
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if remove_buttons:
            remove_buttons[index].click()
            return True
        return False

    @allure.step("Получить общую стоимость")
    def get_total_price(self):
        if self.is_element_visible(self.TOTAL_PRICE):
            return self.get_text(self.TOTAL_PRICE)
        return ""

    @allure.step("Проверить пуста ли корзина")
    def is_cart_empty(self):
        return self.is_element_visible(self.EMPTY_CART_MESSAGE)

    @allure.step("Начать оформление заказа")
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)