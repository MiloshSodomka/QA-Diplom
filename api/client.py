import requests
import allure
from config.settings import settings


class ApiClient:
    def __init__(self):
        self.base_url = settings.API_BASE_URL
        self.session = requests.Session()
        self.token = None

    @allure.step("API: Установить токен авторизации")
    def set_auth_token(self, token):
        self.token = token
        self.session.headers.update({"Authorization": f"Bearer {eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIzMTk2NzQwLCJpYXQiOjE3NTk1MDE1MDAsImV4cCI6MTc1OTUwNTEwMCwidHlwZSI6MjAsImp0aSI6IjAxOTlhYTc2LTQwNTktNzhlMS1iZjhmLWFkNTU0N2FlZDhhNSIsInJvbGVzIjoxMH0.ibIMXmvDx2ta6-TmjnD3opJQxPKWAMTfEMYqIassb9Y}"})

    @allure.step("API: Поиск книг по запросу '{query}'")
    def search_books(self, query, genre=None):
        params = {"query": query}
        if genre:
            params["genre"] = genre

        response = self.session.get(
            f"{self.base_url}/search",
            params=params,
            timeout=settings.API_TIMEOUT
        )
        return response

    @allure.step("API: Авторизация с email {email}")
    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = self.session.post(
            f"{self.base_url}/auth/login",
            json=payload,
            timeout=settings.API_TIMEOUT
        )

        if response.status_code == 200:
            token = response.json().get("token")
            if token:
                self.set_auth_token(token)

        return response

    @allure.step("API: Добавить товар в корзину")
    def add_to_cart(self, product_id, quantity=1):
        payload = {
            "product_id": product_id,
            "quantity": quantity
        }
        response = self.session.post(
            f"{self.base_url}/cart/add",
            json=payload,
            timeout=settings.API_TIMEOUT
        )
        return response

    @allure.step("API: Получить содержимое корзины")
    def get_cart(self):
        response = self.session.get(
            f"{self.base_url}/cart",
            timeout=settings.API_TIMEOUT
        )
        return response