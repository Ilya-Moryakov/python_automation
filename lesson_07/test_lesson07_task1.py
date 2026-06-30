import pytest
from selenium import webdriver
from lesson07_task1 import Calculator


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_slow_calculation(driver):
    calc = Calculator(driver)

    calc.open()

    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    calc.wait_for_result("15", 50)

    assert calc.get_result() == "15"
