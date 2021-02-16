from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_link()

    def should_be_basket_link(self):
        assert 'basket' in self.url, \
            f"Wrong basket link, current_url {self.url}"

    def should_be_no_product_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET), \
            "There is a product in the basket"

    def should_be_product_in_the_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET), \
            "There is not a product in the basket"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
            "Basket is not empty"

    def should_be_not_message_basket_is_emty(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
            "Basket is empty"