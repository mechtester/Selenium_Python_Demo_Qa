from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
import time

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/auto-complete"
driver.get(url)
time.sleep(3)
driver.maximize_window()

mul_color=driver.find_element(By.XPATH,"//body/div[@id='app']/div/div/div/div/div[@id='autoCompleteContainer']/div/div/div[@id='autoCompleteMultiple']/div[@id='autoCompleteMultipleContainer']/div/div[2]")
mul_color.send_keys("red")















