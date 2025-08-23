from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
#driver.get("https://practice.expandtesting.com/dropdown")

#dropdown = Select(driver.find_element(By.ID, "dropdown"))
#dropdown.select_by_visible_text("Option 2")

#checkbox = driver.find_element(By.ID, "checkbox1")
#checkbox.click()


driver = webdriver.Chrome()
driver.get("https://codepen.io/RobotsPlay/pres/pyNLdL")

dropdown = Select(driver.find_element(By.CLASS_NAME, "dropdown-label"))
dropdown.select_by_visible_text("Selection 2")

# Check a checkbox
checkbox = driver.find_element(By.ID, "checkbox1")
checkbox.click()


input("Please Enter to Continue...")