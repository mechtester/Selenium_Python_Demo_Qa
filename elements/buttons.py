from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

"firefox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/buttons"
driver.get(url)

#scroll to location
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)

#double click path
double_click=driver.find_element_by_xpath("//button[normalize-space()='Double Click Me']")
#right click
right_click=driver.find_element_by_xpath("//button[normalize-space()='Right Click Me']")
#click_me
click_me=driver.find_element_by_xpath("//button[normalize-space()='Click Me']")

#create action chanin object
action=ActionChains(driver)
#double click
action.double_click(on_element=double_click)
#perform the action operation
action.perform()
time.sleep(1)
#right click
action.context_click(on_element=right_click)
action.perform()
time.sleep(1)
#click me
action.click(on_element=click_me)
action.perform()

time.sleep(4)
#driver quite command
driver.quit()

print("button section finished")