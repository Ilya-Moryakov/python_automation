from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # Ваш код здесь
    customer_name = driver.find_element(By.NAME, "custname")
    customer_name.send_keys("Ilya Moryakov")

    driver.find_element(By.XPATH, "//button[text()='Submit order']").click()

    assert driver.current_url != "https://httpbin.org/forms/post"

    driver.quit()
