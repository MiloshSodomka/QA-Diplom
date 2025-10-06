import pytest
import allure
from config.settings import settings


@allure.feature("UI Тесты")
@allure.story("Авторизация")
class TestLogin:
    @allure.title("Успешная авторизация")
    def test_successful_login(self, login_page, main_page):
        with allure.step("Открыть страницу авторизации"):
            login_page.open_login_page()

        with allure.step("Ввести валидные учетные данные"):
            login_page.login(settings.TEST_EMAIL, settings.TEST_PASSWORD)

        with allure.step("Проверить успешную авторизацию"):
            assert login_page.is_login_successful(), "Авторизация не выполнена"

    @allure.title("Авторизация с неверным паролем")
    def test_login_with_wrong_password(self, login_page):
        with allure.step("Открыть страницу авторизации"):
            login_page.open_login_page()

        with allure.step("Ввести неверный пароль"):
            login_page.login(settings.TEST_EMAIL, "wrong_password")

        with allure.step("Проверить сообщение об ошибке"):
            error_message = login_page.get_error_message()
            assert error_message, "Сообщение об ошибке не отображается"


@allure.feature("UI Тесты")
@allure.story("Поиск товаров")
class TestSearch:
    @allure.title("Поиск существующей книги")
    def test_search_existing_book(self, main_page, search_page):
        with allure.step("Выполнить поиск книги 'Гарри Поттер'"):
            main_page.search_for_product("Гарри Поттер")

        with allure.step("Проверить наличие результатов поиска"):
            results_count = search_page.get_search_results_count()
            assert results_count > 0, "Результаты поиска не найдены"

    @allure.title("Поиск несуществующей книги")
    def test_search_nonexistent_book(self, main_page, search_page):
        with allure.step("Выполнить поиск несуществующей книги"):
            main_page.search_for_product("абвгд12345несуществующаякнига")

        with allure.step("Проверить сообщение об отсутствии результатов"):
            assert search_page.is_no_results_message_displayed(), \
                "Сообщение об отсутствии результатов не отображается"


@allure.feature("UI Тесты")
@allure.story("Корзина")
class TestCart:
    @allure.title("Добавление товара в корзину")
    def test_add_product_to_cart(self, main_page, search_page, cart_page):
        with allure.step("Найти книгу для добавления в корзину"):
            main_page.search_for_product("Гарри Поттер")

        with allure.step("Добавить первую книгу в корзину"):
            product_title = search_page.get_product_title()
            assert search_page.add_product_to_cart(), "Не удалось добавить товар в корзину"

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        with allure.step("Проверить наличие товара в корзине"):
            cart_items_count = cart_page.get_cart_items_count()
            assert cart_items_count > 0, "Товар не добавлен в корзину"

    @allure.title("Удаление товара из корзины")
    def test_remove_product_from_cart(self, cart_page):
        with allure.step("Перейти в корзину"):
            cart_page.go_to_cart()

        with allure.step("Удалить товар из корзины"):
            if cart_page.get_cart_items_count() > 0:
                cart_page.remove_item_from_cart()

        with allure.step("Проверить что корзина пуста"):
            assert cart_page.is_cart_empty(), "Корзина не пуста после удаления товара"

    @allure.title("Отображение общей стоимости в корзине")
    def test_cart_total_price(self, cart_page):
        with allure.step("Перейти в корзину"):
            cart_page.go_to_cart()

        with allure.step("Проверить отображение общей стоимости"):
            total_price = cart_page.get_total_price()
            assert total_price, "Общая стоимость не отображается"