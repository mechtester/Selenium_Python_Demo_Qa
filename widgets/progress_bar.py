import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Driver
browser = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=browser)

url = "https://demoqa.com/progress-bar"
driver.get(url)
time.sleep(3)
driver.maximize_window()

start_button = driver.find_element(By.XPATH, "//button[@id='startStopButton']")
start_button.click()
time.sleep(3)

progress_bar = driver.find_element(By.XPATH, "//div[@id='progressBar']")

# Wait until the progress bar text is equal to "100%"
wait = WebDriverWait(driver, 10)
element = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='progressBar']"), "100%"))

print(progress_bar.text)
