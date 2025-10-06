import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BASE_URL = "https://www.chitai-gorod.ru"
    API_BASE_URL = "https://api.chitai-gorod.ru"

    # Test data
    TEST_EMAIL = os.getenv("TEST_EMAIL", "test@example.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "password123")

    # Browser settings
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "10"))

    # API settings
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))


settings = Settings()