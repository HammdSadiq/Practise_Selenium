import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage # type: ignore
from pages.inventory_page import InventoryPage # type: ignore
from pages.cart_page import CartPage # type: ignore
from pages.checkout_page import CheckoutPage # type: ignore

def test_complete_order(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Step 1: Login 
    login.load()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Step 3: Checkout
    cart.proceed_to_checkout()
    checkout.enter_info_and_continue("John", "Doe", "12345")
    checkout.finish_order()

    # Step 4: Assertion
    assert "Thank you for your order!" in checkout.get_confirmation_text()

    import time
    time.sleep(15)  # Wait for 15 seconds before closing 
    
