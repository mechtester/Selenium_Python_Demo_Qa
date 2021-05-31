from selenium import webdriver
import time

"firefox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/frames"
driver.get(url)
time.sleep(2)

#get the list of iframe in the web page using tag names
frame=driver.find_elements_by_tag_name("iframe")
print("No of frames in this web page: ", len(frame))

#switch between iframe using real xpath
iframe_big=driver.find_element_by_xpath("//iframe[@id='frame1']")
driver.switch_to.frame(iframe_big)
time.sleep(3)

driver.switch_to.default_content()

#scroll to location
driver.execute_script("window.scrollBy(100,500)","")
time.sleep(2)

iframe_small=driver.find_element_by_xpath("//iframe[@id='frame2']")
driver.switch_to.frame(iframe_small)

driver.quit()