
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

timeout_value = 10
driver = webdriver.Firefox(timeout=timeout_value)# You can use other browser drivers like Firefox, Edge, etc.

    # Open the web pageC:C:\Users\swaro\OneDrive\Desktop\PD\selen\index.html
driver.get("http://localhost:8080/")  # Replace with the actual path

title = driver.title
if title == 'Your Web App - Home':
    print('title:',title)
else: print('error') 

driver.find_element(By.LINK_TEXT,"Home").click()
driver.find_element(By.LINK_TEXT,"Recommendation Board").click()
driver.find_element(By.LINK_TEXT,"Contact Us").click()

driver.close()
