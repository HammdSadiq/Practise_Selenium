from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get("https://www.saucedemo.com")
        # Wait for page to load
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        time.sleep(2)  # Additional wait for page stability

    def login(self, username, password):
        # Wait for login form elements
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        password_field = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        # Wait for login to complete and redirect
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        time.sleep(3)  # Wait for inventory page to fully load