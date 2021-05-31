from selenium import webdriver

import time

"firefox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/upload-download"
driver.get(url)

#download
driver.find_element_by_xpath("//a[normalize-space()='Download']").click()
