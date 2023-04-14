from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/tool-tips"
driver.get(url)
time.sleep(3)
driver.maximize_window()

Hover_me_to_see=driver.find_element(By.XPATH,"//button[@id='toolTipButton']")
Hove_text=driver.find_element(By.XPATH,"//input[@id='toolTipTextField']")

contrary=driver.find_element(By.XPATH,"//a[normalize-space()='Contrary']")
time.sleep(3)
txt_number=driver.find_element(By.XPATH,"//a[normalize-space()='1.10.32']")
time.sleep(5)

#Hover text not completed
ActionChains(driver).move_to_element(Hover_me_to_see).perform()
time.sleep(3)
ActionChains(driver).move_to_element(Hove_text).perform()
time.sleep(3)

driver.execute_script("window.scrollBy(200,300)","")

ActionChains(driver).move_to_element(contrary).perform()
time.sleep(3)
ActionChains(driver).move_to_element(txt_number).perform()
time.sleep(3)







