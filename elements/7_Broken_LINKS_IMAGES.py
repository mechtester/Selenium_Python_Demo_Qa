import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
url="https://demoqa.com/broken"
driver.get(url)
driver.maximize_window()
title=driver.title
assert title == 'ToolsQA'
print("Web Title Matching")

##CLICK FOR VALID LINK
# driver.execute_script("window.scrollBy(0,500)","")
# driver.find_element_by_xpath("//a[normalize-space()='Click Here for Valid Link']").click()
# time.sleep(5)
# driver.back()
# time.sleep(10)

##CLICK FOR BROKEN LINK
# driver.execute_script("window.scrollBy(0,700)","")
# driver.find_element_by_xpath("//a[normalize-space()='Click Here for Broken Link']").click()
# time.sleep(5)
# driver.back()
# time.sleep(10)

product_img_xpath='//div[@class='col-12 mt-4 col-md-6']//img[1]'
imgs = browser.find_elements_by_xpath(product_img_xpath)
for img in imgs:
    actions.move_to_element(img).perform()
    print(img.get_attribute('src'))

driver.close()


