from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "[data-testid='profile-button']")

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.driver.get(f"{self.driver.current_url}/auth")

    @allure.step("Выполнить авторизацию с email {email} и паролем {password}")
    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Получить текст ошибки")
    def get_error_message(self):
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    @allure.step("Проверить успешную авторизацию")
    def is_login_successful(self):
        return self.is_element_visible(self.PROFILE_BUTTON)