import time


class PostLogin:

    def __init__(self, driver):
        self.driver = driver

        self.menu_options_id = "nav-hamburger-menu"

    def menu_click(self, menuoption1, menuoption2):
        self.driver.find_element_by_id(self.menu_options_id).click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains (text(), '" + menuoption1 + "')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains (text(), '" + menuoption2 + "')]").click()
    