from selenium.webdriver.common.by import By

from PageObject.pages import Locators

class BookingConfirm:
    def __init__(self,driver):
        self.order_id = driver.find_element(By.XPATH,Locators.order_id_xpath)


    #getters

    def getOrderId(self):
        return self.order_id

