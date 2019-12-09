
from selenium import webdriver
import unittest
import time
from PageObject.Pages.registerPage import Register
from PageObject.Pages.loginPage import LoginPage
from PageObject.Pages.homePage import HomePage


class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(20)

    def test_register(self):
        driver = self.driver
        driver.get('http://automationpractice.com/')

        signin = HomePage(driver)
        signin.click_signin()

        register_auth = LoginPage(driver)
        register_auth.enter_email_register("gihilav450@mailhub.pro")
        register_auth.click_create()

        register_form = Register(driver)
        register_form.click_title()
        register_form.enter_fname("Ram")
        register_form.enter_lname("Shrestha")
        register_form.enter_password("Test@123")
        register_form.select_dob_days(7)
        register_form.select_dob_month(7)
        register_form.select_dob_year(24)
        register_form.enter_address("test address")
        register_form.enter_city("test city")
        register_form.enter_state("Florida")
        register_form.enter_postalcode("1111")
        register_form.enter_mobile("123456")
        register_form.click_register()

        time.sleep(4)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
