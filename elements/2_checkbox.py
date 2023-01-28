from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

"fire fox driver"
# driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver=webdriver.Edge(executable_path="/usr/local/bin/msedgedriver")

url="https://demoqa.com/checkbox"
driver.get(url)
time.sleep(3)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='app']"))).Click()
#driver.find_element_by_xpath("").click()
#home section
