from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#alogin_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#aregister_form")