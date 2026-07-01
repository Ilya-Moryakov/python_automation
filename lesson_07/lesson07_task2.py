from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.USERNAME_INPUT = (By.ID, "user-name")
        self.PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
        self.LOGIN_BUTTON = (By.NAME, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_id):
        locator = (By.ID, item_id)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.CHECKOUT_BUTTON = (
            By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.POSTAL_CODE = (By.ID, "postal-code")
        self.CONTINUE_BUTTON = (By.ID, "continue")
        self.TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def wait_for_total(self, expected_price):
        self.wait.until(
            EC.text_to_be_present_in_element(self.TOTAL_LABEL, expected_price))

    def get_total_text(self):
        return self.driver.find_element(*self.TOTAL_LABEL).text
