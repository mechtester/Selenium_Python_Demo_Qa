from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import textwrap

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/date-picker"
driver.get(url)
time.sleep(3)
driver.maximize_window()

#click_calender
driver.find_element(By.XPATH,"//input[@id='datePickerMonthYearInput']").click()
time.sleep(3)
a=driver.find_element(By.XPATH,"//input[@id='datePickerMonthYearInput']")
a.send_keys(Keys.CONTROL + "a")
a.send_keys(Keys.DELETE)
a.send_keys("01/11/1990")
a.send_keys(Keys.ENTER)
time.sleep(3)

#Date and time calender
b=driver.find_element(By.XPATH,"//input[@id='dateAndTimePickerInput']")
b.click()
year=driver.find_element(By.XPATH,"//span[@class='react-datepicker__year-read-view--selected-year']")
year.click()

up_arrow=driver.find_element(By.XPATH,"//body//div//div[@data-placement='top-start']//div//div//div//div//div//div//div//div[1]")
down_arrow=driver.find_element(By.XPATH,"//body//div//div[@data-placement='top-start']//div//div//div//div//div//div//div//div[13]")
year_want=driver.find_element(By.XPATH,"//div[normalize-space()='1996']")







