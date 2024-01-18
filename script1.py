import time
import pytest
from selenium.webdriver.common.by import By

class title:
  def test11(self,driver):    
    driver.get("https://www.saucedemo.com/")
    actual_url = driver.current_url
    assert actual_url == "https://www.saucedemo.com/"
