from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.PARTIAL_LINK_TEXT, 'View basket')

class BasketPageLocators:
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, ".basket-itemsa")

class MainPageLocators:
    pass

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