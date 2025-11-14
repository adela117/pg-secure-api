import os

class Settings:
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
