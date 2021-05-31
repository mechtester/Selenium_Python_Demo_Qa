from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"fire fox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.maximize_window()
url="https://demoqa.com/webtables"
driver.get(url)
time.sleep(2)
# scroll to loaction
driver.execute_script("window.scrollBy(0,200)","")

first_name="vignesh"
last_name="kumar"
email="kumarandroid@protonmail.com"
age="25"
salary="100000"
department="quality"
#add deatils
time.sleep(2)
driver.find_element_by_xpath("//button[normalize-space()='Add']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='firstName']").send_keys(first_name)
time.sleep(1)
driver.find_element_by_xpath("//input[@id='lastName']").send_keys(last_name)
time.sleep(1)
driver.find_element_by_xpath("//input[@id='userEmail']").send_keys(email)
time.sleep(1)
driver.find_element_by_xpath("//input[@id='age']").send_keys(age)
time.sleep(1)
driver.find_element_by_xpath("//input[@id='salary']").send_keys(salary)
time.sleep(1)
driver.find_element_by_xpath("//input[@id='department']").send_keys(department)
time.sleep(1)

driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
time.sleep(3)
#close browser
driver.quit()
print("webtables section is completed")
