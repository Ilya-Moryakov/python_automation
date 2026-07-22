import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.DELAY_INPUT: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self.SCREEN_OUTPUT: tuple[str, str] = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу медленного калькулятора")
    def open(self) -> None:
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку {seconds} сек.")
    def set_delay(self, seconds: int | str) -> None:
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT))
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажать на кнопку '{symbol}'")
    def click_button(self, symbol: str) -> None:
        button_xpath: tuple[str, str] = (By.XPATH,
                                         f"//span[text()='{symbol}']")
        button = self.wait.until(EC.element_to_be_clickable(button_xpath))
        button.click()

    @allure.step("Ожидать появления результата '{expected_result}'"
                 " в течение {timeout_seconds} сек.")
    def wait_for_result(self, expected_result: str,
                        timeout_seconds: int) -> None:
        WebDriverWait(self.driver, timeout_seconds).until(
            EC.text_to_be_present_in_element(
                self.SCREEN_OUTPUT, expected_result)
        )

    @allure.step("Получить текущий текст с экрана калькулятора")
    def get_result(self) -> str:
        return self.driver.find_element(*self.SCREEN_OUTPUT).text
