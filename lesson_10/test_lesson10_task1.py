import pytest
import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from lesson10_task1 import Calculator


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@allure.title("Тест медленного калькулятора")
@allure.description("Проверка корректности сложения 7 + 8"
                    " с задержкой в 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculation(driver: WebDriver) -> None:
    calc = Calculator(driver)

    calc.open()
    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    calc.wait_for_result("15", 50)

    with allure.step("Проверить, что на экране отображается результат '15'"):
        result = calc.get_result()
        assert result == "15", f"Ожидалось '15', но на экране: '{result}'"
