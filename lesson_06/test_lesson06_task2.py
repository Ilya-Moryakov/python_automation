from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "OGUxNWUwZGYtOTU1Yi00NzQwLWE1ZjctNzM5YjQ3ODBjZjBk",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/ilyamoryakov")

    user1_url = driver.current_url

    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie({
        "name": "SESSION",
        "value": "ODI1MGQ2MjItN2M3NC00YjdiLWE0MWEtNzkzNjFmYTg3YjM4",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    driver.get("https://gitflic.ru/user/airsworld")

    user2_url = driver.current_url

    assert user1_url != user2_url, "URL совпадают"

    driver.quit()
