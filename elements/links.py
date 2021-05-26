from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

"firefox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
url='https://demoqa.com/links'
driver.get(url)

#get the window handles befor going to new windows
window_before=driver.window_handles[0]
print(window_before)

#scroll to location
driver.execute_script("window.scrollBy(0,200)","")

new_link_1=driver.find_element_by_xpath("//a[normalize-space()='Home']")
new_link_1.click()
time.sleep(4)

#get the window handles after going to new windows
window_after=driver.window_handles[1]
print(window_after)
time.sleep(5 )

#switch to parent window
driver.switch_to.window(window_before)
time.sleep(4)
print(driver.title)

#going to third window
#its a dynamic link its changes rapidly so i use id to capture and open
new_link_2=driver.find_element_by_id("dynamicLink")
new_link_2.click()

window_before1=driver.window_handles[2]
print(window_before1)
time.sleep(5)

#switch to parent window
driver.switch_to.window(window_before)
time.sleep(3)

#link to get api messages
driver.find_element_by_xpath("//a[normalize-space()='Created']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[normalize-space()='No Content']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[normalize-space()='Moved']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[normalize-space()='Bad Request']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[normalize-space()='Unauthorized']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[normalize-space()='Forbidden']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[normalize-space()='Not Found']").click()
time.sleep(2)

time.sleep(4)
driver.quit()

print("link section finished")
