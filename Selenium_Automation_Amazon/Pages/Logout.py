class Logout:

    def __init__(self, driver):
        self.driver = driver

        self.logout_id = "nav-link-accountList"
        self.logout_link_id = "nav-item-signout"

    def signout_click(self):
        #action = ActionChains(self.driver)
        #action.move_to_element(self.logout_id).perform()
        #self.driver.find_element_by_id(self.logout_link_id).click()

