from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import textwrap

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/accordian"
driver.get(url)
time.sleep(3)
driver.maximize_window()

#scroll to location
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)

# first question
first_question=driver.find_element(By.XPATH,"(//div[@id='section1Heading'])[1]")
first_question.click()
a=first_question.text
print(a)

#wrap text
a_ans=driver.find_element(By.CSS_SELECTOR,"div[id='section1Content'] p")
ns=a_ans.text
wrap_1=textwrap.fill(ns, width=90)
print(wrap_1)
time.sleep(3)

# second question
second_question=driver.find_element(By.XPATH,"(//div[@id='section2Heading'])[1]")
second_question.click()
b=second_question.text
print(b)
time.sleep(4)
#scrolling to location
driver.execute_script("window.scrollBy(0,500)","")
#wrap text
b_ans=driver.find_element(By.CSS_SELECTOR,"#section2Content")
ns1=b_ans.text
wrap_2=textwrap.fill(ns1, width=90)
print(wrap_2)

#third question
third_question=driver.find_element(By.XPATH,"(//div[@id='section3Heading'])[1]")
third_question.click()
c=third_question.text
print(c)
time.sleep(3)
br_ans=driver.find_element(By.CSS_SELECTOR,"div[id='section3Content'] p")
ns13=br_ans.text
wrap_3=textwrap.fill(ns13, width=90)
print(wrap_3)

print("ACCORDIAN SECTION FINISHED")

driver.quit()
