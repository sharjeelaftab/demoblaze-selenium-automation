from selenium.webdriver.common.by import By
import time

class ViewCart:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self) -> None:
        self.driver.find_element(By.ID, "cartur").click()
        time.sleep(2)