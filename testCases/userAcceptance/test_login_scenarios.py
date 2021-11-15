import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from selenium.webdriver.common.by import By
chrome_driver_path = "/driversWindows/chromedriver_win32/chromedriver.exe"


# for using Geckodriver
# driver = webdriver.Firefox(executable_path="driversWindows/geckodriver-v0.30.0-win64/geckodriver.exe")

# navigate to the url

@pytest.mark.teat_verifying_url
def test_verifying_url():
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('http://the-internet.herokuapp.com/login')
    #printing the title of the web page
    print(driver.title)
    driver.close()



# Verifying the fields
@pytest.mark.test_verifying_fields
def test_verifying_fields():

    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element_by_name("username").is_enabled()
    driver.find_element_by_name("password").is_enabled()
    driver.find_element_by_xpath("//button[@class='radius']").is_displayed()
    driver.close()



# Verifying the error message for wrong username
@pytest.mark.test_verifying_wrong_username
def test_verifying_wrong_username():
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('http://the-internet.herokuapp.com/login')


    driver.find_element_by_name("username").send_keys("abcd")
    driver.find_element_by_name("password").send_keys("abcd")
    driver.find_element_by_xpath("//button[@class='radius']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[contains(text(),'Your username is invalid!')]").is_displayed()
    driver.close()





# verifying the error message for wrong password
@pytest.mark.test_verifying_wrong_password
def test_verifying_wrong_password():
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('http://the-internet.herokuapp.com/login')

    driver.find_element_by_name("username").send_keys("tomsmith")
    driver.find_element_by_name("password").send_keys("abcd")
    driver.find_element_by_xpath("//button[@class='radius']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[contains(text(),'Your password is invalid!')]").is_displayed()
    driver.close()




# verifying the login scenario with correct ID and password
@pytest.mark.test_logged_in
def test_verifying_logged_in():
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element_by_name("username").send_keys("tomsmith")
    driver.find_element_by_name("password").send_keys("SuperSecretPassword!")
    driver.find_element_by_xpath("//button[@class='radius']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[contains(text(),'You logged into a secure area!')]").is_displayed()
    driver.find_element_by_xpath("//*[contains(text(),'Logout')]").is_displayed()
    driver.close()


@pytest.mark.test_logged_out
def test_verifying_logged_out():
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element_by_name("username").send_keys("tomsmith")
    driver.find_element_by_name("password").send_keys("SuperSecretPassword!")
    driver.find_element_by_xpath("//button[@class='radius']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[contains(text(),'You logged into a secure area!')]").is_displayed()
    driver.find_element_by_xpath("//*[contains(text(),'Logout')]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[contains(text(),'Login Page')]").is_displayed()
    driver.close()

