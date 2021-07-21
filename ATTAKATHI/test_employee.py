from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from libglobal.LibGlobal import Base
import pytest
import allure

class TestBowserLaunch(Base):
    @pytest.fixture()
    def setup(self):

        self.driver = self.launch_browser()
        self.window_maximize()
        self.load_url("https://en-gb.facebook.com/")
        yield
        self.browser_quit()
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username,password",[("ashok","ashok@123"),("arun","arun@123"),("bala","bala@123"),("parthi","parthi@123")])
    def test_login(self,setup,username,password):
        txt_username = self.driver.find_element(By.ID,"email")
        self.send_txt(txt_username,username)
        txt_password = self.driver.find_element(By.ID, "pass")
        self.send_txt(txt_password,password)
        btn_login = self.driver.find_element(By.XPATH,"//button[@value='1']")
        self.btn_click(btn_login)
        allure.attach(self.driver.get_screenshot_as_png(),name="sample",attachment_type=AttachmentType.PNG)




from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_launchbrowser(self):
        driver  = webdriver.Chrome(executable_path=r"C:\Users\DELL\PycharmProjects\SELENIUM\Driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://en-gb.facebook.com/")
        url = driver.current_url
        assert "xyw" in url
        text_username = driver.find_element(By.ID,"email")
        text_username.send_keys("123456789")

    def test_payment(self):
        print("payment...")

    def test_addition(self):
        print("ten"+10)
