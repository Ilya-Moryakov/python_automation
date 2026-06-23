from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(
        By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.NAME, "login-button")
    login_button.click()

    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    checkout_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
    ))
    checkout_button.click()

    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("first")

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("last")

    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "summary_total_label"), "58.29"
    ))

    price_total = driver.find_element(
        By.CLASS_NAME, "summary_total_label").text
    assert "58.29" in price_total, (
        f"The result was expected to be $58.29, "f" but on the screen:"
        f" {price_total}")

    driver.quit()
