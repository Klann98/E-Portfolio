from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time


driver = webdriver.Chrome()

driver.get("http://localhost:8000/blog/")
original_blog_count = len(driver.find_elements_by_id("blogs"))

driver.get("http://localhost:8000/admin/login/?next=/admin/")
elem = driver.find_element_by_name("username")
elem.send_keys("marcus")

elem = driver.find_element_by_name("password")
elem.send_keys("password123")
elem.send_keys(Keys.RETURN) #pressing enter
time.sleep(2)

driver.get("http://localhost:8000/admin/blog/post/add/")
time.sleep(2)

elem = driver.find_element_by_name("title")
elem.send_keys("Testing Blog Posting")

elem = driver.find_element_by_name("body")
elem.send_keys("")

from selenium.webdriver.support.ui import Select

elem = Select(driver.find_element_by_name("categories"))
elem.select_by_value('2')

elem = driver.find_element_by_name("_save") 
elem.click()

driver.get("http://localhost:8000/blog/")
assert len(driver.find_elements_by_id("blogs")) == original_blog_count


driver.close()
