
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_saucedemo_end_to_end(driver):

    # 1. Login
    login = LoginPage(driver)
    login.open_website()
    login.login()

    # 2. Verify products
    inventory = InventoryPage(driver)
    inventory.verify_products_page()
    assert inventory.get_product_count() > 0

    # 3. Add product to cart
    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == "1"

    # 4. Open cart and verify product
    inventory.open_cart()
    cart = CartPage(driver)
    assert cart.verify_backpack_in_cart()

    # 5. Proceed to checkout
    cart.click_checkout()

    print("URL after checkout click:", driver.current_url)
    assert "checkout-step-one.html" in driver.current_url

    # 6. Enter customer details
    checkout = CheckoutPage(driver)
    checkout.enter_customer_details()

    # 7. Complete the order
    checkout.finish_checkout()

    # 8. Verify completed order
    checkout.verify_order_success()

    # 9. Return to products page
    checkout.return_home()

    # 10. Logout
    inventory.logout()
    login.verify_login_page()
