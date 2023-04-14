import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/links"
driver.maximize_window()
driver.get(url)


title=driver.title

if title == 'DEMOQA':
   print("Web Title Matching")
else:
    print("Web Title Not Matched")

#CLICK FOR VALID LINK
driver.execute_script("window.scrollBy(100,200)","")
a=driver.current_window_handle
print("Link page handle:",a)

# #Click home button
# driver.find_element(By.XPATH,"//a[@id='simpleLink']").click()
# LINK=driver.current_url
# print("Link Page URL:",LINK)
#
# driver.switch_to.window(driver.window_handles[1])
# home_page_handle=driver.current_window_handle
# print("Home page handle:",home_page_handle)
# LINK_1=driver.current_url
# print("HOME Page URL:",LINK_1)

#Back to link page
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.execute_script("window.scrollBy(100,100)","")
print("scrolled")
time.sleep(5)
################################################
# #Api call clicking
# define a list of XPATHs for the links you want to click on
links = ["//a[@id='created']", "//a[@id='no-content']", "//a[@id='moved']", "//a[@id='bad-request']", "//a[@id='unauthorized']", "//a[@id='forbidden']" , "//a[@id='invalid-url']"]

# loop through the list of XPATHs and click on each link
for link in links:
    time.sleep(2)
    element = driver.find_element(By.XPATH, link)
    element.click()

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#linkResponse")))

    link_response=driver.find_element(By.CSS_SELECTOR,"#linkResponse")
    print(link_response.text)
