from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        register_new_user_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        register_new_user_email.send_keys(email)

        register_new_user_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        register_new_user_password.send_keys(password)

        register_new_user_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        register_new_user_password2.send_keys(password)

        register_new_user_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_new_user_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, \
            f"Wrong login url this {self.url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"