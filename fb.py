from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.facebook.com/')

email_input = driver.find_element_by_name(
    "email").send_keys("")
passwd = driver.find_element_by_name("pass").send_keys("")

signin_button = driver.find_element_by_id("loginbutton").click()
