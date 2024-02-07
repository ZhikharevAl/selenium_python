"""selenium example"""
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(5)
