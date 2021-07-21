from selenium.webdriver.common.by import By

from PageObject.pages import Locators

class LoginPage:
    def __init__(self,driver):
        self.txt_username = driver.find_element(By.ID,Locators.username_id)
        self.txt_password = driver.find_element(By.ID,Locators.password_id)
        self.btn_login = driver.find_element(By.ID,Locators.btn_login_id)

    #getters
    def getTxtUserName(self):
        return self.txt_username
    def getTxtPassword(self):
        return self.txt_password
    def getBtnLogin(self):
        return self.btn_login
