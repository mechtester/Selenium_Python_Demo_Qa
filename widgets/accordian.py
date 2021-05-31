from selenium import webdriver
import time

"firefox driver"
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/accordian"
driver.get(url)
time.sleep(3)

#scroll to location
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)

# first question
first_question=driver.find_element_by_id("section1Heading")
first_question.click()
time.sleep(3)

# second question
second_question=driver.find_element_by_id("section2Heading")
second_question.click()
time.sleep(4)
second_question.click()
time.sleep(3)

#third question
third_question=driver.find_element_by_id("section3Heading")
third_question.click()
time.sleep(3)

driver.quit()

print("ACCORDIAN SECTION FINISHED")