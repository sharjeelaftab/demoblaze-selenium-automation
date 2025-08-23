from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v136.fed_cm import click_dialog_button
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


#driver.get("https://www.daraz.pk/")
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/span[1]/*[name()='svg'][1]/*[name()='path'][1]")


#driver.get("https://petstore.octoperf.com/")
#driver.find_element(By.LINK_TEXT, "Enter the Store").click()
#driver.implicitly_wait(10)
#driver.find_element(By.LINK_TEXT, "Sign In").click()
#driver.find_element(By.TAG_NAME,"input").send_keys("Sharjeel")
#driver.find_element(By.PARTIAL_LINK_TEXT,"Sign")
#driver.find_element(By.NAME,"keyword").send_keys("Test")


#driver.get("https://www.daraz.pk/")
#driver.find_element(By.CLASS_NAME,"search-box__input--O34g").send_keys("Watches")
#driver.find_element(By.ID,"q").send_keys("Exercise Machine")




input("Please Enter to Continue...")


