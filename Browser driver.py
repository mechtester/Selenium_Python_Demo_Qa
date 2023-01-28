from selenium import webdriver
import time

"fire fox driver"
# driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver=webdriver.Edge(executable_path="/usr/local/bin/msedgedriver")

options= webdriver.ChromeOptions()
options.binary_location="/usr/bin/google-chrome"
chrome_driver_binary="/usr/local/bin/chromedriver"
# driver=webdriver.Chrome(chrome_driver_binary,chrome_options=options)
# driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")


url="https://demoqa.com/checkbox"
driver.get(url)
time.sleep(3)
