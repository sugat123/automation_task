from selenium.webdriver.support.ui import Select


class Register():

    def __init__(self, driver):
        self.driver = driver

        self.pi_title_id = "id_gender1"
        self.pi_f_name_id = "customer_firstname"
        self.pi_l_name_id = "customer_lastname"
        self.pi_password_input_id = "passwd"
        self.pi_dob_days_id = "days"
        self.pi_dob_months_id = "months"
        self.pi_dob_year_id = "years"

        # address_fname = driver.find_element_by_id("firstname").send_keys(fname)
        # address_lname = driver.find_element_by_id("lastname").send_keys(lname)
        self.address1_id = "address1"
        self.city_id = "city"
        self.state_id = "id_state"
        self.postal_code_id = "postcode"
        self.mobile_id = "phone_mobile"
        self.register_button_id = "submitAccount"

    def click_title(self):
        self.driver.find_element_by_id(self.pi_title_id).click()

    def enter_fname(self, fname):
        self.driver.find_element_by_id(self.pi_f_name).send_keys(fname)

    def enter_lname(self, lname):
        self.driver.find_element_by_id(self.pi_l_name).send_keys(lname)

    def enter_password(self, password):
        self.driver.find_element_by_id(
            self.pi_password_input_id).send_keys(password)

    def select_dob_days(self, days):
        self.Select(driver.find_element_by_id(
            self.pi_dob_days_id)).select_by_index(days)

    def select_dob_month(self, month):
        self.Select(driver.find_element_by_id(
            self.pi_dob_months_id)).select_by_index(month)

    def select_dob_year(self, year):
        self.Select(driver.find_element_by_id(
            self.pi_dob_year_id)).select_by_index(year)

    def enter_address(self, address):
        self.driver.find_element_by_id(self.address1_id).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element_by_id(self.city_id).send_keys(city)

    def enter_state(self, state):
        self.Select(driver.find_element_by_id(self.state_id)
                    ).select_by_visible_text(state)

    def enter_postalcode(self, postalcode):
        self.driver.find_element_by_id(
            self.postal_code_id).send_keys(postalcode)

    def enter_mobile(self, mobile):
        self.driver.find_element_by_id(self.mobile_id).send_keys(mobile)

    def click_register(self):
        self.driver.driver.find_element_by_id(self.register_button_id).click()
