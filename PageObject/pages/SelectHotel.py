from selenium.webdriver.common.by import By

from PageObject.pages import Locators

class SelectHotel:
    def __init__(self,driver):
        self.btn_select = driver.find_element(By.XPATH,Locators.btn_select_xpath)
        self.btn_continue = driver.find_element(By.XPATH,Locators.btn_continue_xpath)

    #getters

    def getBtnSelectHotel(self):
        return self.btn_select
    def getBtnContinue(self):
        return self.btn_continue
