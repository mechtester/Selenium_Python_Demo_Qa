from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Chrome Driver
browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser)

url="https://demoqa.com/nestedframes"
driver.get(url)

time.sleep(3)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='frame1']"))
frame_text = driver.find_element(By.TAG_NAME,'body').text
print(frame_text)


inside_frame = driver.find_element(By.XPATH,"//iframe[@srcdoc='<p>Child Iframe</p>']")
driver.switch_to.frame(inside_frame)

text=driver.find_element(By.XPATH,"//p[normalize-space()='Child Iframe']")
print(text.text)
