import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser=Service(executable_path="/usr/local/bin/msedgedriver")
driver=webdriver.Edge(service=browser)

url="https://demoqa.com/broken"
driver.get(url)
driver.maximize_window()

title=driver.title

if title == 'DEMOQA':
   print("Web Title Matching")
else:
    print("Web Title Not Matched")

#CLICK FOR VALID LINK
driver.execute_script("window.scrollBy(0,500)","")

#Click for valid link
driver.find_element(By.XPATH,"//a[normalize-space()='Click Here for Valid Link']").click()
a=driver.current_url
print(a)
driver.back()

#Click for in-valid link
driver.find_element(By.XPATH,"//a[normalize-space()='Click Here for Broken Link']").click()
b=driver.current_url
print(b)

f=driver.find_element(By.XPATH,"//p[contains(text(),'This page returned a 500 status code.')]").text
print(f)

driver.close()


