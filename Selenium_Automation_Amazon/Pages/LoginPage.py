class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.login_txtbox_id = "ap_email"
        self.continue_button_id = "continue"
        self.password_txtbox_id = "ap_password"
        self.signin_button_id = "signInSubmit"

    def applogin(self, username, password):
        self.driver.find_element_by_id(self.login_txtbox_id).send_keys(username)
        self.driver.find_element_by_id(self.continue_button_id).click()
        self.driver.find_element_by_id(self.password_txtbox_id).send_keys(password)
        self.driver.find_element_by_id(self.signin_button_id).click()
