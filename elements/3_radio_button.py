from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
import time

"Chrome driver"
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)
driver.maximize_window()

url="https://demoqa.com/radio-button"
driver.get(url)

driver.find_element(By.XPATH,"//label[normalize-space()='Yes']").click()
Ye=driver.find_element(By.XPATH,"//span[@class='text-success']").text
print("You have selected:",Ye)
time.sleep(3)
driver.find_element(By.XPATH,"//label[normalize-space()='Impressive']").click()
Yew=driver.find_element(By.XPATH,"//span[@class='text-success']").text
print("You have selected:",Yew)
time.sleep(3)
