
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import TIMEOUT


class CartPage:

    BACKPACK = (
        By.XPATH,
        "//div[@class='inventory_item_name' "
        "and text()='Sauce Labs Backpack']"
    )

    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='checkout']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def verify_backpack_in_cart(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.BACKPACK)
        ).is_displayed()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

        self.wait.until(
            EC.url_contains("checkout-step-one.html")
        )
