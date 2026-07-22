import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.USERNAME_INPUT: tuple[str, str] = (By.ID, "user-name")
        self.PASSWORD_INPUT: tuple[str, str] = (By.CSS_SELECTOR,
                                                "input[name='password']")
        self.LOGIN_BUTTON: tuple[str, str] = (By.NAME, "login-button")

    @allure.step("Открыть главную страницу магазина")
    def open(self) -> None:
        self.driver.get("https://saucedemo.com")

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> None:
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.CART_LINK: tuple[str, str] = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товар с ID '{item_id}' в корзину")
    def add_to_cart(self, item_id: str) -> None:
        locator: tuple[str, str] = (By.ID, item_id)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        self.driver.find_element(*self.CART_LINK).click()


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.CHECKOUT_BUTTON: tuple[str, str] = (
            By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")

    @allure.step("Нажать на кнопку Checkout")
    def checkout(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.FIRST_NAME: tuple[str, str] = (By.ID, "first-name")
        self.LAST_NAME: tuple[str, str] = (By.ID, "last-name")
        self.POSTAL_CODE: tuple[str, str] = (By.ID, "postal-code")
        self.CONTINUE_BUTTON: tuple[str, str] = (By.ID, "continue")
        self.TOTAL_LABEL: tuple[str, str] = (By.CLASS_NAME,
                                             "summary_total_label")

    @allure.step("Заполнить форму оформления заказа: {first_name} {last_name},"
                 " индекс: {postal_code}")
    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Ожидать отображения итоговой суммы '{expected_price}'")
    def wait_for_total(self, expected_price: str) -> None:
        self.wait.until(
            EC.text_to_be_present_in_element(self.TOTAL_LABEL, expected_price))

    @allure.step("Получить итоговый текст суммы")
    def get_total_text(self) -> str:
        return self.driver.find_element(*self.TOTAL_LABEL).text
