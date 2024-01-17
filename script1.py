import time
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

         driver.get("http://localhost:8000")
      title = driver.title

# Check if the title is as expected
   expected_title = "Your Web App - Home"
         assert title == expected_title, f"Title mismatch. Expected: {expected_title}, Actual: {title}"

driver.quit()
