import pytest
import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from lesson10_task2 import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


@allure.title("Тест покупки товаров в интернет-магазине")
@allure.description("Авторизация, добавление трех товаров в корзину"
                    " и проверка финальной стоимости на этапе Checkout")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(driver: WebDriver) -> None:
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_form("first", "last", "123456")
    checkout_page.wait_for_total("58.29")

    with allure.step("Проверить, что итоговая сумма включает '$58.29'"):
        price_total = checkout_page.get_total_text()
        assert "58.29" in price_total, (
            f"The result was expected to be $58.29, "
            f"but on the screen: {price_total}"
        )
