from selenium import webdriver
import time
"fire fox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
url="https://demoqa.com/radio-button"
driver.get(url)


driver.find_element_by_xpath("//label[normalize-space()='Yes']").click()
time.sleep(3)
driver.find_element_by_xpath("//label[normalize-space()='Impressive']").click()
print("radio button section finished")