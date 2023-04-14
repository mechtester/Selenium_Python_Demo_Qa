from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service

# Create a new Service object
service = Service("/usr/local/bin/chromedriver")

# Pass the Service object to the Chrome driver
driver = webdriver.Chrome(service=service)

url="https://demoqa.com/modal-dialogs"
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
