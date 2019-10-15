from .locators import BasePageLocators
from .base_page import BasePage

class CartPage(BasePage):
    def should_basket_be_empty(self):
        self.should_not_be_products()
        self.should_be_empty_cart_message()

    def should_not_be_products(self):
        assert not self.is_element_present(*BasePageLocators.BASKET_NOT_EMPTY_FORM), "Basket not empty, because there is a basket_formset"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_TEXT), "Basket empty text is not presented"
