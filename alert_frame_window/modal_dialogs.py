from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"firefox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/modal-dialogs"
driver.get(url)

time.sleep(3)

small_modal=driver.find_element_by_xpath("//button[normalize-space()='Small modal']")
small_modal.click()

element= WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "closeSmallModal")))
time.sleep(3)
element.click()
time.sleep(3)
large_modal=driver.find_element_by_xpath("//button[normalize-space()='Large modal']")
large_modal.click()

big_element = driver.find_element_by_xpath("//button[normalize-space()='Close']")
time.sleep(3)
big_element.click()

driver.quit()

print("model dialogs section finished")
