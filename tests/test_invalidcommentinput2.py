from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/blog/1/")

original_comment_count = len(driver.find_elements_by_class_name("comment"))

elem = driver.find_element_by_name("author")
elem.send_keys("annonymus")

elem = driver.find_element_by_name("body")
elem.send_keys("")
elem = driver.find_element_by_id("submitcomment") 
elem.click()
time.sleep(2)


assert len(driver.find_elements_by_class_name("comment")) == original_comment_count
driver.close()
