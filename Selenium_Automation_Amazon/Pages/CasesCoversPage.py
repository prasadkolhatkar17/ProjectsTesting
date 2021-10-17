import time

from selenium.webdriver.support.ui import Select


class CasesCoversPage:

    def __init__(self, driver):
        self.driver = driver
        self.quantity_drpdown_id = "quantity"
        self.add_cart_button_id = "add-to-cart-button"
        self.shop_cart_id = "nav-cart"

    def product_to_select(self, productname):
        self.driver.find_element_by_xpath(
            "//div[@class = 'bxc-grid__image   bxc-grid__image--light']/a/img[@alt = '" + productname + "']").click()
        casescoverlst = self.driver.find_elements_by_xpath(
            "//div[@class='a-section a-spacing-none a-spacing-top-small']//a")
        casescoverlst[2].click()

        parentwin = self.driver.current_window_handle
        chdwin = self.driver.window_handles
        for w in chdwin:
            if w != parentwin:
                self.driver.switch_to.window(w)
                break
        self.Add_item_tocart()
        # Assert "Added to Cart" in self.driver.page_source
        self.confirm_delete()

    def Add_item_tocart(self):
        time.sleep(15)
        select_quantity = Select(self.driver.find_element_by_id(self.quantity_drpdown_id))
        select_quantity.select_by_visible_text("2")
        self.driver.find_element_by_id(self.add_cart_button_id).click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@id='nav-cart']").click()

    def confirm_delete(self):
        self.driver.find_element_by_xpath("//span[@class='a-declarative']/input[@value='Delete']").click()
