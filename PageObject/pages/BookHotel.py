from selenium.webdriver.common.by import By

from PageObject.pages import Locators

class BookHotel:
    def __init__(self,driver):
        self.txt_first_name = driver.find_element(By.XPATH,Locators.first_name_xpath)
        self.txt_last_name = driver.find_element(By.XPATH,Locators.last_name_xpath)
        self.txt_address = driver.find_element(By.XPATH,Locators.address_xpath)
        self.credit_card_no = driver.find_element(By.XPATH, Locators.credit_card_no_xpath)
        self.credit_card_type = driver.find_element(By.XPATH, Locators.credit_card_type_xpath)
        self.select_month = driver.find_element(By.XPATH, Locators.select_month_xpath)
        self.select_year = driver.find_element(By.XPATH, Locators.select_year_xpath)
        self.ccv_no = driver.find_element(By.XPATH, Locators.ccv_no_xpath)
        self.btn_book = driver.find_element(By.XPATH, Locators.btn_book_xpath)

    #getters

    def getFirstName(self):
        return self.txt_first_name
    def getLastName(self):
        return self.txt_last_name
    def getAddress(self):
        return self.txt_address
    def getCreditCardNo(self):
        return self.credit_card_no
    def getCreditCardType(self):
        return self.credit_card_type
    def getSelectMonth(self):
        return self.select_month
    def getSelectYear(self):
        return self.select_year
    def getCcvNo(self):
        return self.ccv_no
    def getBtnBook(self):
        return self.btn_book

