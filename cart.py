from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_name):
        wait = WebDriverWait(self.driver, 10)

        for attempt in range(3):
            try:
                product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name)))
                product.click()
                break
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                time.sleep(1)


        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
        add_to_cart_btn.click()


        alert = wait.until(EC.alert_is_present())
        print("Alert text:", alert.text)
        alert.accept()


        home_link = wait.until(EC.element_to_be_clickable((By.ID, "nava")))
        home_link.click()

        time.sleep(2)


