
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import (
    BASE_URL,
    USERNAME,
    PASSWORD,
    TIMEOUT
)


class LoginPage:

    USERNAME_FIELD = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open_website(self):
        self.driver.get(BASE_URL)

    def login(self):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        ).send_keys(USERNAME)

        self.driver.find_element(
            *self.PASSWORD_FIELD
        ).send_keys(PASSWORD)

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    def verify_login_page(self):
        self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_BUTTON)
        )
