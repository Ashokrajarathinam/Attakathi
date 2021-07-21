from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome(executable_path=r"C:\Users\DELL\PycharmProjects\SELENIUM\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(10)
cls = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
driver.execute_script("arguments[0].click()",cls)
search_txt = driver.find_element(By.XPATH,"//input[@name='q']")
driver.execute_script("arguments[0].setAttribute('value','iphone')",search_txt)
btn_click = driver.find_element(By.XPATH,"//button[@class='L0Z3Pu']")
btn_click.click()


















