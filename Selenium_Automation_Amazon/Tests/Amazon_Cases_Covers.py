from selenium import webdriver
import unittest
import time
from Selenium_Automation_Amazon.Pages.HomePage import HomePage
from Selenium_Automation_Amazon.Pages.PostLogin import PostLogin
from Selenium_Automation_Amazon.Pages.CasesCoversPage import CasesCoversPage



class CasesCovers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= "C:/Users/Kolhatkar/PycharmProjects/WebSampleProject/Selenium_Automation_Amazon/Drivers_exe/chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_CasesCovers(self):
        # ******** Object created for individual Pages ***************** #
        driver = self.driver
        homepg = HomePage(driver)
        postloginpg = PostLogin(driver)
        casecoverpg = CasesCoversPage(driver)


        # ***************************************** #

        # *********************** Execution of Test ************************ #

        driver.get("http://www.amazon.in")
        postloginpg.menu_click("Mobiles, Computers","Cases & Covers")
        casecoverpg.product_to_select("samsung")
        time.sleep(5)


        # ***************************************** #

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
