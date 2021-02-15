from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main p')
    MESSAGE_ADD_TO_BASKET_NAME_PRODUCT = (By.CSS_SELECTOR, '.alertinner strong')
    MESSAGE_ADD_PRODUCT_TO_PRODUCT = (By.CSS_SELECTOR, '.alertinner')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alertinner p strong')