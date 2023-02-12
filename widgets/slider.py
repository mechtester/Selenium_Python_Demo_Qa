from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import textwrap
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/slider"
driver.get(url)
time.sleep(3)
driver.maximize_window()

slider = driver.find_element(By.XPATH,"//input[@type='range']")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(10, 0).release().perform()

time.sleep(3)
