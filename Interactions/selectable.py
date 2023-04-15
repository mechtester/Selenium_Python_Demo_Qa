from selenium import webdriver
import time
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

## Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)
driver.maximize_window()
url="https://demoqa.com/selectable"
driver.get(url)

# print(":::List section::::")
# time.sleep(3)
# element_1=driver.find_element(By.XPATH,"//li[normalize-space()='Cras justo odio']")
# element_1.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,200)","")
# element_2=driver.find_element(By.XPATH,"//li[normalize-space()='Dapibus ac facilisis in']")
# element_2.click()
# element_3=driver.find_element(By.XPATH,"//li[normalize-space()='Morbi leo risus']")
# element_3.click()
# element_4=driver.find_element(By.XPATH,"//li[normalize-space()='Porta ac consectetur ac']")
# element_4.click()
# time.sleep(4)

#Grid Section
driver.find_element(By.ID,"demo-tab-grid").click()
time.sleep(5)
driver.find_element(By.XPATH,"//li[normalize-space()='One']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[normalize-space()='Two']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[normalize-space()='Three']").click()
time.sleep(3)
driver.execute_script("window.scrollBy(100,200)","")
driver.find_element(By.XPATH,"//li[normalize-space()='Four']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[normalize-space()='Five']").click()
time.sleep(3)

