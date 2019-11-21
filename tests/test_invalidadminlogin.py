from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/admin/login/?next=/admin/")
elem = driver.find_element_by_name("username")
elem.send_keys("user")

elem = driver.find_element_by_name("password")
elem.send_keys("password123")
elem.send_keys(Keys.RETURN) #pressing enter
time.sleep(2)

assert driver.current_url == 'http://localhost:8000/admin/login/?next=/admin/'


driver.close()
