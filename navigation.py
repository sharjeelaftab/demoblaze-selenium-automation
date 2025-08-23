from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


class Navigation:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def open_site(self, url="https://demoblaze.com/index.html"):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def assert_title(self, expected_title):
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Expected {expected_title}, but got {actual_title}"

    def click_signup(self):
        self.driver.find_element(By.ID, "signin2").click()
        time.sleep(1)

    def click_login(self):
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(1)

    def quit(self):
        time.sleep(2)
        self.driver.quit()

