from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self):
        # Wait for checkout button to be clickable
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        
        # Wait for checkout page to load
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        time.sleep(3)  # Wait for checkout page to fully load
        