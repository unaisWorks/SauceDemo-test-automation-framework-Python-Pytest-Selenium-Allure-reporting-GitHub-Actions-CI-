import os

BASE_URL = "https://www.saucedemo.com/"

USERNAME = os.getenv("SAUCEDEMO_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCEDEMO_PASSWORD", "secret_sauce")

TIMEOUT = 10
BROWSER = os.getenv("BROWSER", "chrome")