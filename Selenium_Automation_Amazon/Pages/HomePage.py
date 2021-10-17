from selenium.webdriver.common.action_chains import ActionChains
import time


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_signin(self, driver):
        # self.driver.find_element_by_id(self.signin_button_id).click()
        action = ActionChains(driver)
        parent_element = self.driver.find_element_by_xpath("//a[@id = 'nav-link-accountList']")
        action.move_to_element(parent_element).perform()
        time.sleep(5)
        child_element = self.driver.find_element_by_xpath("//span[@class = 'nav-action-inner']")
        child_element.click()
