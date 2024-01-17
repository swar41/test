import time
import pytest
from selenium.webdriver.common.by import By


class TestLoginPage:
    def test_valid_login(self, driver):
        driver.get("http://localhost:8000/")
        # time.sleep(2)

         actual_url = driver.current_url
        assert actual_url == "http://localhost:8000/"

        # time.sleep(2)
