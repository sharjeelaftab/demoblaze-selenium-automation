from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v136.fed_cm import click_dialog_button
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://demo.applitools.com/app.html")
driver.find_element(By.XPATH,"//i[@class='os-icon os-icon-mail-14']")


input("Please Enter to Continue...")


