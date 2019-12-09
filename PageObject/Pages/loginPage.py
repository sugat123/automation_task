class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_input_register_id = "email_create"
        self.create_button_id = "SubmitCreate"
        self.email_input_login_id = "email"
        self.passwd_id = "passwd"
        self.signin_button_id = "SubmitLogin"

    def enter_email_register(self, email):
        self.driver.find_element_by_id(self.email_input_register_id).clear()
        self.driver.find_element_by_id(self.email_input_register_id).send_keys(email)

    def click_create(self):
        self.driver.find_element_by_id(self.create_button_id).click()

    def enter_email_login(self, email):
        self.driver.find_element_by_id(self.email_input_id).clear()
        self.driver.find_element_by_id(self.email_input_id).send_keys(email)

    def enter_passwd(self, passwd):
        self.driver.find_element_by_id(self.passwd_id).clear()
        self.driver.find_element_by_id(self.passwd_id).send_keys(passwd)

    def click_login(self):
        self.driver.find_element_by_id(self.signin_button_id).click()
