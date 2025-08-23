from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://candymapper.com/")

driver.find_element(By.ID, "popup-widget307423-close-icon").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Scroll up again
driver.execute_script("window.scrollTo(0, 0);")

input("Please Enter to Continue...")