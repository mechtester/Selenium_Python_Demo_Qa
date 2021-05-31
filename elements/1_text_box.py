from selenium import webdriver
import time
"fire fox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/"

fullname="V.VIGNESHKUMAR"
email="kumarandroid@protonmail.com"
current_address="1/166 NORTH STREET,"
permenant_address="INDIA"

driver.get(url)
driver.maximize_window()
time.sleep(3)
#ELEMENTS
driver.find_element_by_xpath("//*[name()='path' and contains(@d,'M16 132h41')]").click()
#text box
driver.find_element_by_xpath("//span[normalize-space()='Text Box']").click()
#fullname
driver.find_element_by_xpath("//input[@id='userName']").send_keys(fullname)
time.sleep(2)
#email
driver.find_element_by_xpath("//input[@id='userEmail']").send_keys(email)
time.sleep(2)
#current address
driver.find_element_by_xpath("//textarea[@id='currentAddress']").send_keys(current_address)
time.sleep(2)
#permanaet address
driver.find_element_by_xpath("//textarea[@id='permanentAddress']").send_keys(permenant_address)
time.sleep(2)
#scroll to submit button using length method of web page
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
#submit
driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
print("TEXT BOX SECTION FINISHED")

