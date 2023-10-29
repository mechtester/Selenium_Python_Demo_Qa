from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.keys import Keys
import time

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/browser-windows"

driver.get(url)
driver.maximize_window()
time.sleep(3)

# store home tab handle as a 0 value
windows_before=driver.window_handles[0]

#open a new tab
new_tab=driver.find_element(By.XPATH,"//button[normalize-space()='New Tab']")
new_tab.click()
print("HOME TAB:%s"%driver.title)
#store new tab handle as a 1 value
windows_after=driver.window_handles[1]
time.sleep(5)


#switch back to home tab
driver.switch_to.window(windows_before)
print("Back to old home page")
time.sleep(3)

#open a small tab
small_tab=driver.find_element(By.XPATH,"//button[normalize-space()='New Window']")
small_tab.click()
print("SMALL TAB:%s"%driver.title)
#store small tab window handle value as  2
windows_small=driver.window_handles[2]
time.sleep(3)

#open new window message
windows_message=driver.find_element(By.XPATH,"//button[normalize-space()='New Window Message']")
windows_message.click()
print("MESSAGE TAB:%s"%driver.title)
#store window message tab handle value as 3
message_tab=driver.window_handles[3]
time.sleep(5)

driver.quit()


