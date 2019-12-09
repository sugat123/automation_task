class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.signin_button_xpath = "//a[@class='login']"

    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()
