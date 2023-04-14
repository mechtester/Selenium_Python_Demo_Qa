from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Create a new Service object
service = Service("/usr/local/bin/chromedriver")

# Pass the Service object to the Chrome driver
driver = webdriver.Chrome(service=service)

url="https://demoqa.com/nestedframes"
driver.get(url)

time.sleep(3)

# parent_frame=driver.find_element(By.XPATH,"//iframe[@id='frame1']")
# child_frame=driver.find_element(By.CSS_SELECTOR,"body:nth-child(2) > iframe:nth-child(1)")

# driver.switch_to.frame("frame1")
# a=driver.find_element(By.TAG_NAME,"bodytag")
# print(a.text)
# time.sleep(2)
# driver.find_element(By.XPATH,"(//html)[1]").click()

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='frame1']"))
frame_text = driver.find_element(By.TAG_NAME,'body').text
print(frame_text)


inside_frame = driver.find_element(By.XPATH,"//iframe[@srcdoc='<p>Child Iframe</p>']")
driver.switch_to.frame(inside_frame)

text=driver.find_element(By.XPATH,"//p[normalize-space()='Child Iframe']")
print(text.text)
