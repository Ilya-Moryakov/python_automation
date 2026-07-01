from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
        self.SCREEN_OUTPUT = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, seconds):
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT))
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, symbol):
        button_xpath = (By.XPATH, f"//span[text()='{symbol}']")
        button = self.wait.until(EC.element_to_be_clickable(button_xpath))
        button.click()

    def wait_for_result(self, expected_result, timeout_seconds):
        WebDriverWait(self.driver, timeout_seconds).until(
            EC.text_to_be_present_in_element(
                self.SCREEN_OUTPUT, expected_result)
        )

    def get_result(self):
        return self.driver.find_element(*self.SCREEN_OUTPUT).text
