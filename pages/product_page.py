from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_the_basket()
        self.should_be_message_added_to_the_basket_name_product()
        self.should_be_message_added_to_the_basket_total()

    def add_product_to_the_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_message_added_to_the_basket_name_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET_NAME_PRODUCT).text
        assert product_name in message, f"Product has not been added to cart. Product name {product_name}"

    def should_be_message_added_to_the_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price in basket_total, f"Cart price does not match the product price. Product price {product_price}, basket_price {basket_total}"