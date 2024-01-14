
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest

def setup(request):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)# You can use other browser drivers like Firefox, Edge, etc.

    # Open the web pageC:C:\Users\swaro\OneDrive\Desktop\PD\selen\index.html
driver.get("http://localhost:8080/")  # Replace with the actual path

title = driver.title
if title == 'Enabler':
    print('title:',title)
else: print('error') 

driver.find_element(By.LINK_TEXT,"Home").click()
driver.find_element(By.LINK_TEXT,"Recommendation Board").click()
driver.find_element(By.LINK_TEXT,"Contact Us").click()

driver.close()
