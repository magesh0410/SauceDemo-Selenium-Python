
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import FIRST_NAME, LAST_NAME, POSTAL_CODE, TIMEOUT


class CheckoutPage:

    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def enter_customer_details(self):
        print("Current URL:", self.driver.current_url)
        print("Page title:", self.driver.title)

        print("Page source contains first-name:",
              "first-name" in self.driver.page_source)

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME_FIELD
            )
        ).send_keys(FIRST_NAME)

        self.driver.find_element(
            *self.LAST_NAME_FIELD
        ).send_keys(LAST_NAME)

        self.driver.find_element(
            *self.POSTAL_CODE_FIELD
        ).send_keys(POSTAL_CODE)

        self.driver.find_element(
            *self.CONTINUE_BUTTON
        ).click()

    def finish_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def verify_order_success(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text

        assert message == "Thank you for your order!"
        print("ORDER COMPLETED SUCCESSFULLY!")

    def return_home(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACK_HOME_BUTTON)
        ).click()
