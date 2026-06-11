from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # Ваш код здесь
    all_links = driver.find_elements(By.TAG_NAME, "a")

    total_links = len(all_links)
    if total_links == 10:
        print(f"Количество ссылок равно {total_links}.")
    else:
        print(f"Количество ссылок не равно {total_links}.")

    all_displayed = True
    for link in all_links:
        if not link.is_displayed():
            all_displayed = False
            print(f"Ссылка '{link.text}' не отображается.")

    if all_displayed:
        print("Все ссылки отображаются на странице.")

    if total_links > 0:
        first_link_text = all_links[0].text
        if "1" in first_link_text:
            print(f"Текст первой ссылки ('{first_link_text}') содержит '1'.")
        else:
            print(f"Текст первой ссылки "
                  f"('{first_link_text}') не содержит '1'.")

    driver.quit()
