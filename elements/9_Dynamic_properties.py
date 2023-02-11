import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



browser=Service(executable_path="/usr/local/bin/msedgedriver")
driver=webdriver.Edge(service=browser)

url="https://demoqa.com/dynamic-properties"
driver.get(url)
driver.maximize_window()

mywait=WebDriverWait(driver,(10))

login_button_colour = Color.from_string(driver.find_element(By.ID,'colorChange').value_of_css_property('color'))
print(login_button_colour)
time.sleep(10)
# if login_button_colour == login_button_colour:
#     time.sleep(10)

"""Need to Modify code here to add wait
and if condition for value changes."""

login_text_colour = Color.from_string(driver.find_element(By.ID,'colorChange').value_of_css_property('color'))
print(login_text_colour)

if login_text_colour != login_button_colour:
    print("Color change button: Color is changed")

driver.quit()
