from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import  Service

"Chrome driver"
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/checkbox"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
# time.sleep(3)
driver.find_element(By.XPATH,"(//button[@title='Toggle'])[1]").click()
# time.sleep(2)
driver.find_element(By.XPATH,"(//button[@title='Toggle'])[2]").click()
# time.sleep(2)
driver.find_element(By.XPATH,"(//button[@title='Toggle'])[3]").click()
# time.sleep(2)

#scroll to submit button using length method of web page
driver.execute_script("window.scrollBy(0,500)","")

driver.find_element(By.XPATH,"(//button[@title='Toggle'])[4]").click()
# time.sleep(2)
driver.find_element(By.XPATH,"(//button[@title='Toggle'])[5]").click()
# time.sleep(2)
driver.find_element(By.XPATH,"(//button[@title='Toggle'])[6]").click()
# time.sleep(2)

a=driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='check-box-tree-wrapper']/div[@id='tree-node']/ol/li[1]").text
x=a
print(x)
print(len(x))

time.sleep(5)
driver.quit()
