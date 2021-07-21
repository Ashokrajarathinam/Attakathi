import datetime
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Employee(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\DELL\PycharmProjects\SELENIUM\Driver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://en-gb.facebook.com/")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def setUp(self):
        d = datetime.datetime.now()
        print(d)
    def tearDown(self):
        d = datetime.datetime.now()
        print(d)

    def test_login(self):
        text_username = self.driver.find_element(By.ID, "email")
        text_username.send_keys("123456789")
        att = text_username.get_attribute("value")
        self.assertNotEqual("1234567890",att, "verify passed")
        txt_password = self.driver.find_element(By.ID,"pass")
        txt_password.send_keys("hello")
    @unittest.skip("i am ignoring now")
    def test_payment(self):
        print("payment....")
    @unittest.skip
    def test_booking(self):
        print("booking..")
    @unittest.skipIf(condition= 1!= 1,reason="condition is true so iam skipped")
    def test_ashok(self):
        print("ashokraina")





