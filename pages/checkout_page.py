from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_info_and_continue(self, first, last, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish_order(self):
        self.driver.find_element(By.ID, "finish").click()

    def get_confirmation_text(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text