from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    first_name_input = driver.find_element(By.NAME, "first-name")
    first_name_input.send_keys("Иван")

    last_name_input = driver.find_element(By.NAME, "last-name")
    last_name_input.send_keys("Петров")

    address_input = driver.find_element(
        By.CSS_SELECTOR, "input[name='address']")
    address_input.send_keys("Ленина, 55-3")

    email_input = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email_input.send_keys("test@skypro.com")

    phone_number_input = driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']")
    phone_number_input.send_keys("+7985899998787")

    zip_code_input = driver.find_element(By.NAME, "zip-code")
    zip_code_input.send_keys("")

    city_input = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    city_input.send_keys("Москва")

    country_input = driver.find_element(
        By.CSS_SELECTOR, "input[name='country']")
    country_input.send_keys("Россия")

    job_position_input = driver.find_element(By.NAME, "job-position")
    job_position_input.send_keys("QA")

    company_input = driver.find_element(
        By.CSS_SELECTOR, "input[name='company']")
    company_input.send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    zip_code_alert = driver.find_element(By.ID, "zip-code")
    assert (
        "alert-danger" in zip_code_alert.get_attribute("class")
    ), "The field is not red!"

    green_fields_ids = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
    ]

    for field_id in green_fields_ids:
        element = driver.find_element(By.ID, field_id)
        element_class = element.get_attribute("class")
        assert "alert-success" in element_class, f"The field {field_id} is not green!"

    driver.quit()
