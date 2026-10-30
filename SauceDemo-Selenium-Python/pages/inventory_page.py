
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import TIMEOUT


class InventoryPage:

    PRODUCTS_TITLE = (By.XPATH, "//span[text()='Products']")
    PRODUCTS = (By.CSS_SELECTOR, ".inventory_item")

    ADD_BACKPACK = (
        By.CSS_SELECTOR,
        "[data-test='add-to-cart-sauce-labs-backpack']"
    )

    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")

    MENU_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def verify_products_page(self):
        self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        )

    def get_product_count(self):
        return len(
            self.driver.find_elements(*self.PRODUCTS)
        )

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK)
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        ).click()
