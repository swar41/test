import time
import pytest
from selenium.webdriver.common.by import By


class TestLoginPage:
    def test_valid_login(self, driver):
        driver.get("http://localhost:8000/")
        # time.sleep(2)

        # Type username
       title = driver.title
           if title == "Your Web App - Home":
                print('title:',title)
             else: print('error') 

        # time.sleep(2)
