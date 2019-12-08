from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

email = 'gihilav450@mailhub.pro'
fname = "Raju"
lname = "Lama"
password = "Test@123"
address = 'test, test'
phn = '1234567890'

# driver = webdriver.Firefox(executable_path='./geckodriver')
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(40)

driver.get('http://automationpractice.com/')

sign_in = driver.find_element_by_xpath("//a[@class='login']").click()
email_input = driver.find_element_by_id(
    "email_create").send_keys(email)
create_button = driver.find_element_by_id("SubmitCreate").click()

pi_title = driver.find_element_by_id("id_gender1").click()
pi_f_name = driver.find_element_by_id("customer_firstname").send_keys(fname)
pi_l_name = driver.find_element_by_id("customer_lastname").send_keys(lname)
pi_password_input = driver.find_element_by_id("passwd").send_keys(password)
pi_dob_days = Select(driver.find_element_by_id("days")
                     ).select_by_index(7)
pi_dob_months = Select(driver.find_element_by_id(
    "months")).select_by_index(7)
pi_dob_year = Select(driver.find_element_by_id("years")
                     ).select_by_index(24)

# address_fname = driver.find_element_by_id("firstname").send_keys(fname)
# address_lname = driver.find_element_by_id("lastname").send_keys(lname)
address1 = driver.find_element_by_id("address1").send_keys(address)
city = driver.find_element_by_id("city").send_keys('test city')
state = Select(driver.find_element_by_id("id_state")
               ).select_by_visible_text('Florida')
postal_code = driver.find_element_by_id("postcode").send_keys('11111')
mobile = driver.find_element_by_id("phone_mobile").send_keys(phn)

register_button = driver.find_element_by_id("submitAccount").click()

driver.close()
