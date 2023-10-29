from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/frames"
driver.get(url)
driver.maximize_window()
time.sleep(2)

#get the list of iframe in the web page using tag names
frame=driver.find_elements(By.TAG_NAME,"iframe")
print("No of frames in this web page: ", len(frame))

#switch between iframe using real xpath
iframe_big=driver.find_element(By.XPATH,"//iframe[@id='frame1']")
driver.switch_to.frame(iframe_big)
time.sleep(3)

driver.switch_to.default_content()

#scroll to location
driver.execute_script("window.scrollBy(100,500)","")
time.sleep(2)

iframe_small=driver.find_element(By.XPATH,"//iframe[@id='frame2']")
driver.switch_to.frame(iframe_small)

driver.quit()
