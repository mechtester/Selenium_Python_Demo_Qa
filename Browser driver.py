from selenium import webdriver
import time
from selenium.webdriver.chrome.service import  Service

### LINUX WEB DRIVER ####
# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

#Gecokodriver
browser=Service(executable_path="/usr/local/bin/geckodriver")
driver=webdriver.Firefox(service=browser)

#Edge Driver
browser=Service(executable_path="/usr/local/bin/msedgedriver")
driver=webdriver.Edge(service=browser)

url="https://demoqa.com/checkbox"
driver.get(url)
time.sleep(3)
