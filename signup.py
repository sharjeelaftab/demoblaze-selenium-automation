from selenium.webdriver.common.by import By

class Signup:
    def __init__(self, driver):
        self.driver = driver

    def click_signup(self):
        self.driver.find_element(By.ID, "signin2").click()

    def type_username(self, username="Sharjeel"):
        self.driver.find_element(By.ID, "sign-username").send_keys(username)

    def type_password(self, password="Test@123"):
        self.driver.find_element(By.ID, "sign-password").send_keys(password)

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, "//button[text()='Sign up']").click()