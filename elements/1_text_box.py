from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

"Chrome driver"
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)
driver.maximize_window()

url="https://demoqa.com/text-box"

fullname="V.VIGNESHKUMAR"
email="v.vigneshkumar@protonmail.com"
current_address="1/166 NORTH STREET,"
permenant_address="INDIA"

driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.implicitly_wait(10)

#fullname
a=driver.find_element(By.XPATH,"//input[@id='userName']").send_keys(fullname)

#email
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys(email)
#current address
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys(current_address)
#permanaet address
driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys(permenant_address)

#scroll to submit button using length method of web page
driver.execute_script("window.scrollBy(0,500)","")

#submit
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()

# q=driver.find_element(By.CSS_SELECTOR,".border.col-md-12.col-sm-12").text
q=driver.find_element(By.XPATH,"//div[@class='border col-md-12 col-sm-12']").text

print("Text Box Printed Text:\n",q)

driver.quit()
