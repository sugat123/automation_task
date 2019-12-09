
class Locator(object):

    # homepage
    sign_in = "//a[@class='login']"

    # authentication
    email_input_register = "email_create"
    create_button = "SubmitCreate"
    email_input_login = "email"
    passwd = "passwd"
    signin_button = "SubmitLogin"

    # registration
    pi_title = "id_gender1"
    pi_f_name = "customer_firstname"
    pi_l_name = "customer_lastname"
    pi_password_input = "passwd"
    pi_dob_days = "days"
    pi_dob_months = "months"
    pi_dob_year = "years"
    # address_fname = driver.find_element_by_id("firstname").send_keys(fname)
    # address_lname = driver.find_element_by_id("lastname").send_keys(lname)
    address1 = "address1"
    city = "city"
    state = "id_state"
    postal_code = "postcode"
    mobile = "phone_mobile"

    register_button = "submitAccount"

    # locators for buying item and checking out
    cart = "//a[@class='button ajax_add_to_cart_button btn btn-default']"

    category1 = "//ul[@class='submenu-container clearfix first-in-line-xs']//ul//li//a[contains(text(),'T-shirts')]"

    close1 = "//span[@class='cross']"

    category2 = "//li[@class='sfHover']//ul//li//a[contains(text(),'Casual Dresses')]"

    checkout = "//a[@class='btn btn-default button button-medium']"

    checkout2 = "//a[@class='button btn btn-default standard-checkout button-medium']"

    checkout3 = "//button[@name='processAddress']"

    terms = "cgv"

    checkout4 = "//button[@name='processCarrier']"

    payment = "//a[@class='bankwire']"

    confirm_order = "//button[@class='button btn btn-default button-medium']"
