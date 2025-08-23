from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(By.ID, "login2").click()

    def type_username(self, username="Sharjeel"):
        self.driver.find_element(By.ID, "loginusername").send_keys(username)

    def type_password(self, password="Test@123"):
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()