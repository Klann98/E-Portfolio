import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost:8000/projects/')
driver.close()
