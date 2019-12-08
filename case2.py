from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = 'sugatp454@gmail.com'
password = "Test@123"

driver = webdriver.Chrome('./chromedriver')
# driver = webdriver.Firefox(executable_path='./geckodriver')
driver.implicitly_wait(40)


driver.get('http://automationpractice.com/')

sign_in = driver.find_element_by_class_name("login").click()

email_input = driver.find_element_by_id("email").send_keys(email)
passwd = driver.find_element_by_id("passwd").send_keys(password)

# password.send_keys(Keys.RETURN)
signin_button = driver.find_element_by_id("SubmitLogin").click()
# signin_button.click()
# driver.switch_to_window("dashboard")
# WebDriverWait(driver, 10).until(EC.title_contains("My account - My Store"))


# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Dresses')))
# element.click()
cart_xpath = "//a[@class='button ajax_add_to_cart_button btn btn-default']"

category1 = driver.find_element_by_xpath(
    "//ul[@class='submenu-container clearfix first-in-line-xs']//ul//li//a[contains(text(),'T-shirts')]").click()
cart1 = driver.find_element_by_xpath(cart_xpath).click()

close1 = driver.find_element_by_xpath(
    "//span[@class='cross']").click()

category2 = driver.find_element_by_xpath(
    "//li[@class='sfHover']//ul//li//a[contains(text(),'Casual Dresses')]").click()
cart2 = driver.find_element_by_xpath(cart_xpath).click()

checkout = driver.find_element_by_xpath(
    "//a[@class='btn btn-default button button-medium']").click()

checkout2 = driver.find_element_by_xpath(
    "//a[@class='button btn btn-default standard-checkout button-medium']").click()

checkout3 = driver.find_element_by_xpath(
    "//button[@name='processAddress']").click()

terms = driver.find_element_by_id("cgv").click()

checkout4 = driver.find_element_by_xpath(
    "//button[@name='processCarrier']").click()

payment = driver.find_element_by_xpath(
    "//a[@class='bankwire']").click()

confirm_order = driver.find_element_by_xpath(
    "//button[@class='button btn btn-default button-medium']").click()
