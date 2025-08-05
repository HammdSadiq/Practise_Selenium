from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_item_to_cart(self):
        # Wait for inventory items to load
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        time.sleep(2)  # Wait for page stability
        
        # Find and click the first add to cart button
        add_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory")))
        add_button.click()
        time.sleep(2)  # Wait for cart update

    def go_to_cart(self):
        # Wait for cart link to be clickable
        cart_link = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_link.click()
        
        # Wait for cart page to load
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
        time.sleep(3)  # Wait for cart page to fully load