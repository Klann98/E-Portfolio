import os
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost:8000/blog/')
time.sleep(2)
driver.close()
