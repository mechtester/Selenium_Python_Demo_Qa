from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

"Chrome driver"
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)
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
driver.find_element(By.XPATH,"//span[@id='delete-record-1']").click()
driver.find_element(By.XPATH,"//span[@id='delete-record-2']").click()
driver.find_element(By.XPATH,"//span[@id='delete-record-3']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//button[@id='addNewRecordButton']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys(first_name)
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys(last_name)
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys(email)
driver.find_element(By.XPATH,"//input[@id='age']").send_keys(age)
driver.find_element(By.XPATH,"//input[@id='salary']").send_keys(salary)
driver.find_element(By.XPATH,"//input[@id='department']").send_keys(department)
time.sleep(3)
driver.find_element(By.XPATH,"//button[@id='submit']").click()
time.sleep(3)

a=driver.find_element(By.XPATH, "//div[@class='rt-tbody']").text
print(a)

driver.quit()
print("webtables section is completed")
