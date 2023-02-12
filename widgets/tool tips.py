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
txt_number=driver.find_element(By.XPATH,"//a[normalize-space()='1.10.32']")
time.sleep(2)

#Hover text not completed








