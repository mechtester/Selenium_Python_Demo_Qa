from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
import time


# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/alerts"

driver.get(url)
driver.maximize_window()
time.sleep(3)

#####SCROLLING FOR SPECIFIC FUNCTION#########
driver.execute_script("window.scroll(0,100)","")

#1alert pop up
alert=driver.find_element(By.XPATH,"//button[@id='alertButton']")
alert.click()
time.sleep(3)

#switch to alert window
alert_box=driver.switch_to.alert
#get message from alert window printing a alert message in .text format
message=alert_box.text
print("Alert shows following message: "+message)
time.sleep(3)
#this command for acceptaing a ok button
alert_box.accept()


#2late_alert winodw
late_alert=driver.find_element(By.XPATH,"//button[@id='timerAlertButton']")
late_alert.click()

#explict wait
WebDriverWait(driver, 6).until(EC.alert_is_present())

#switch to late alert window
late=driver.switch_to.alert
late_message=late.text
time.sleep(3)
late.accept()
print("late alert shows following message: "+late_message)
time.sleep(4)

#3confirm box
confirm_box=driver.find_element(By.XPATH,"//button[@id='confirmButton']")
confirm_box.click()

#switch to confirm box
confirm=driver.switch_to.alert
time.sleep(4)
message=confirm.text
print("confirm box shows following message: "+message)
confirm.accept()

#4promot box
promot_box=driver.find_element(By.XPATH,"//button[@id='promtButton']")
promot_box.click()
#switch to promot box
promot=driver.switch_to.alert
message=promot.text
print("promot box shows following message: "+message)
promot.send_keys("VIGNESHKUMAR")
time.sleep(3)
promot.accept()
time.sleep(4)

driver.quit()

print("alert section finished")
