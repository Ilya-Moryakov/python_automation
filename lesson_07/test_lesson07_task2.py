import pytest
from selenium import webdriver
from lesson07_task2 import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


def test_shop(driver):
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

    price_total = checkout_page.get_total_text()
    assert "58.29" in price_total, (
        f"The result was expected to be $58.29,"
        f" but on the screen: {price_total}"
    )
