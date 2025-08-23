from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Checkout:
    def __init__(self, driver):
        self.driver = driver

    def place_order(self, name, country, city, credit_card, month, year):
        place_order_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
        place_order_btn.click()
        time.sleep(2)

        # Fill out the form
        self.driver.find_element(By.ID, "name").send_keys("Sharjeel Malik")
        self.driver.find_element(By.ID, "country").send_keys("Pakistan")
        self.driver.find_element(By.ID, "city").send_keys("Lahore")
        self.driver.find_element(By.ID, "card").send_keys("424242424242")
        self.driver.find_element(By.ID, "month").send_keys("08")
        self.driver.find_element(By.ID, "year").send_keys("2026")


        purchase_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")
        purchase_btn.click()
        time.sleep(3)

        confirmation = self.driver.find_element(By.XPATH, "//div[@class='sweet-alert  showSweetAlert visible']/h2").text
        print("Order Confirmation:", confirmation)

        # Close confirmation
        ok_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'OK')]")
        ok_btn.click()
        time.sleep(2)
