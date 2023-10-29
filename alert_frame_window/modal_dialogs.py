from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/modal-dialogs"
driver.maximize_window()
driver.get(url)

time.sleep(3)

small_modal=driver.find_element(By.XPATH,"//button[normalize-space()='Small modal']")
small_modal.click()

element= WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "closeSmallModal")))
time.sleep(3)
element.click()
time.sleep(3)
large_modal=driver.find_element(By.XPATH,"//button[normalize-space()='Large modal']")
large_modal.click()

big_element = driver.find_element(By.XPATH,"//button[normalize-space()='Close']")
time.sleep(3)
big_element.click()

driver.quit()

print("model dialogs section finished")
