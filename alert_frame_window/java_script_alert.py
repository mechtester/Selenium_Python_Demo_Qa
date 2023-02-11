from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
driver.maximize_window()
time.sleep(3)

#click js alert
clcik_js_alert=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
clcik_js_alert.click()
time.sleep(3)

#Extract text from js alert
alert=driver.switch_to.alert
alert_text=alert.text
print(alert_text)
alert.accept()

#click for js confirm
clcik_js_confirm=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
clcik_js_confirm.click()
time.sleep(3)

#Extract text from js confirm
alert_1=driver.switch_to.alert
alert_text_1=alert_1.text
print(alert_text_1)
alert.accept()

#click for js prompt
clcik_js_prompt=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
clcik_js_prompt.click()
time.sleep(3)

#Extract text from js confirm
alert_1=driver.switch_to.alert
alert_text_1=alert_1.text
print(alert_text_1)
alert.send_keys("Hello I am testing")
time.sleep(3)
alert.accept()
time.sleep(3)
