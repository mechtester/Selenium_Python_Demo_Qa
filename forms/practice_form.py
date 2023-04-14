from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.support.ui import WebDriverWait
import time

"Chrome driver"
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)
url="https://demoqa.com/automation-practice-form"
driver.get(url)
driver.maximize_window()
time.sleep(3)


"scrolling for specific location"
driver.execute_script("window.scrollBy(0,200)","")
"i dont know why %s and % is used "
print("Page title :%s"%driver.title)

#form details
first_name="vignesh"
last_name="kumar"
email="kumar@gmail.com"
mobile="9876543210"
subjects="maths"
address="india"
full_address="1/16 big building , chennai , Tamilnadu"

#paths
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys(first_name)
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys(last_name)
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys(email)
time.sleep(2)
driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys(mobile)
time.sleep(2)

#click to open date picker
date_picker=driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']")
date_picker.click()

#choose month
select=Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']"))
#select by visible text method
select.select_by_index(2)

# choose year
select=driver.find_element(By.XPATH,"//option[@value='1996']")
#select by visible text method
select.click()

#choose date
wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'13')]"))).click()
time.sleep(2)

#subjects select
subject=driver.find_element(By.ID,"subjectsContainer")
time.sleep(3)
subject.click()

actions=ActionChains(driver)
actions.move_to_element(subject).send_keys("english").perform()
time.sleep(3)
englsish=driver.find_element(By.XPATH,"//div[contains(text(),'English')]")
englsish.click()

actions=ActionChains(driver)
actions.move_to_element(subject).send_keys("maths").perform()
time.sleep(3)
maths=driver.find_element(By.XPATH,"//div[contains(text(),'Maths')]")
maths.click()

#hobbies select
sports=driver.find_element(By.XPATH,"//label[normalize-space()='Sports']")
sports.click()
time.sleep(2)
reading=driver.find_element(By.XPATH,"//label[normalize-space()='Reading']")
reading.click()
time.sleep(2)
music=driver.find_element(By.XPATH,"//label[normalize-space()='Music']")
music.click()
time.sleep(2)

#upload picture
upload_path=input("Enter Upload File Path:")
upload=driver.find_element(By.XPATH,"//input[@id='uploadPicture']")
upload.send_keys(upload_path)
time.sleep(3)

"scrolling for specific location"
driver.execute_script("window.scrollBy(200,250)","")
#enter address
current_address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
current_address.click()
current_address.send_keys(full_address)
time.sleep(3)

"scrolling for specific location"
driver.execute_script("window.scrollBy(250,350)","")
driver.execute_script("document.body.style.zoom='60%'")
time.sleep(5)

#select state
# wait for the state element to be clickable
# state = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Select State')]")))

# click on the state element
# state.click()

time.sleep(2)

# states=driver.find_element(By.XPATH,"//div[contains(text(),'Rajasthan')]")
# states.click()
# time.sleep(2)
#
# #select city
# city=driver.find_element(By.XPATH,"//div[contains(text(),'Select City')]")
# city.click()
# time.sleep(3)
#
# citys=driver.find_element(By.XPATH,"//div[contains(text(),'Jaipur')]")
# citys.click()
# time.sleep(3)

# #submit button
# submit=driver.find_element(By.XPATH,"//button[@id='submit']")
# submit.click()

time.sleep(5)
driver.quit()

