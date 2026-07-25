from src.core.config import get_settings

settings = get_settings()

print(settings.APP_NAME)
print(settings.APP_VERSION)
print(settings.APP_PORT)