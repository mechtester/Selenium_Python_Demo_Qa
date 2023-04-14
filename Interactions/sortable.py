from selenium import webdriver
import time
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

## Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)
driver.maximize_window()
url="https://demoqa.com/sortable"
driver.get(url)

print("::::List Section::::")
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(3)
a=driver.find_element(By.XPATH,"//div[@class='vertical-list-container mt-4']")
print("::::Before Changing numbers order::::")
print(a.text)

#  div[id='demo-tabpane-list'] div div:nth-child(6)
#number change order code
number_1= driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div[@role='tabpanel']/div/div[1]")
position_6= driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div[@role='tabpanel']/div/div[6]")
ActionChains(driver).drag_and_drop(number_1, position_6).perform()

number_2= driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div[@role='tabpanel']/div/div[2]")
position_5= driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div[@role='tabpanel']/div/div[5]")
ActionChains(driver).drag_and_drop(number_2, position_5).perform()

number_3= driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div[@role='tabpanel']/div/div[3]")
position_4= driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div[@role='tabpanel']/div/div[4]")
ActionChains(driver).drag_and_drop(number_3, position_4).perform()

b=driver.find_element(By.XPATH,"//div[@class='vertical-list-container mt-4']")
print("::::After Changing numbers order::::")
print(b.text)
time.sleep(5)

print("::::Grid Section::::")
driver.find_element(By.XPATH,"//a[@id='demo-tab-grid']").click()

First_position=driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[1]")
six_position=driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[6]")
ActionChains(driver).drag_and_drop(First_position, six_position).perform()


second_position=driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[2]")
four_position=driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[4]")
ActionChains(driver).drag_and_drop(second_position, four_position).perform()

three_position=driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[3]")
six_position=driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[6]")
ActionChains(driver).drag_and_drop(three_position, six_position).perform()
time.sleep(5)
