from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"fire fox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/alerts"

driver.get(url)
driver.maximize_window()
time.sleep(3)

#1alert pop up
alert=driver.find_element_by_xpath("//button[@id='alertButton']")
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
late_alert=driver.find_element_by_xpath("//button[@id='timerAlertButton']")
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
confirm_box=driver.find_element_by_xpath("//button[@id='confirmButton']")
confirm_box.click()

#switch to confirm box
confirm=driver.switch_to.alert
time.sleep(4)
message=confirm.text
print("confirm box shows following message: "+message)
confirm.accept()

#4promot box
promot_box=driver.find_element_by_xpath("//button[@id='promtButton']")
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