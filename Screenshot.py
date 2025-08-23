from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.applitools.com/app.html")
driver.save_screenshot("applitools_screenshot.png")
driver.quit()

input("Please Enter to Continue...")