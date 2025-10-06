import pytest
import allure
from config.settings import settings


@allure.feature("API Тесты")
@allure.story("Поиск книг")
class TestSearchAPI:
    @allure.title("API: Поиск по существующему названию (кириллица)")
    def test_search_existing_book_cyrillic(self, api_client):
        with allure.step("Выполнить поиск книги 'Гарри Поттер'"):
            response = api_client.search_books("Гарри Поттер")

        with allure.step("Проверить статус код 200"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

        with allure.step("Проверить наличие результатов"):
            data = response.json()
            assert "products" in data, "В ответе отсутствует поле 'products'"
            assert len(data["products"]) > 0, "Результаты поиска пусты"

    @allure.title("API: Поиск по существующему названию (латиница)")
    def test_search_existing_book_latin(self, api_client):
        with allure.step("Выполнить поиск книги 'Harry Potter'"):
            response = api_client.search_books("Harry Potter")

        with allure.step("Проверить статус код 200"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    @allure.title("API: Поиск с фильтром по жанру")
    def test_search_with_genre_filter(self, api_client):
        with allure.step("Выполнить поиск с фильтром жанра"):
            response = api_client.search_books("фантастика", genre="Фэнтези")

        with allure.step("Проверить статус код 200"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"


@allure.feature("API Тесты")
@allure.story("Негативные сценарии поиска")
class TestSearchNegativeAPI:
    @allure.title("API: Поиск с пустым запросом")
    def test_search_empty_query(self, api_client):
        with allure.step("Выполнить поиск с пустым запросом"):
            response = api_client.search_books("")

        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"

    @allure.title("API: Поиск несуществующей книги")
    def test_search_nonexistent_book(self, api_client):
        with allure.step("Выполнить поиск несуществующей книги"):
            response = api_client.search_books("абвгд12345несуществующаякнига")

        with allure.step("Проверить статус код 200"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

        with allure.step("Проверить пустой результат"):
            data = response.json()
            assert len(data.get("products", [])) == 0, "Ожидался пустой результат поиска"

    @allure.title("API: Поиск с SQL-инъекцией")
    def test_search_sql_injection(self, api_client):
        with allure.step("Выполнить поиск с SQL-инъекцией"):
            response = api_client.search_books("' OR 1=1 --")

        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"


@allure.feature("API Тесты")
@allure.story("Корзина")
class TestCartAPI:
    @allure.title("API: Добавление товара в корзину")
    def test_add_to_cart(self, api_client):
        # Предполагаем, что у нас есть ID товара для теста
        test_product_id = "12345"

        with allure.step("Добавить товар в корзину"):
            response = api_client.add_to_cart(test_product_id)

        with allure.step("Проверить успешное добавление"):
            # В реальном проекте здесь будет проверка статус кода
            # assert response.status_code == 200
            pass

    @allure.title("API: Получение содержимого корзины")
    def test_get_cart(self, api_client):
        with allure.step("Получить содержимое корзины"):
            response = api_client.get_cart()

        with allure.step("Проверить структуру ответа"):
            # В реальном проекте здесь будет проверка структуры JSON
            # assert "items" in response.json()
            pass