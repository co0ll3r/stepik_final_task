import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException 

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_form()
        self.should_be_add_to_basket_button()
        self.should_be_write_review_button()
        self.should_add_product_to_basket()
        self.should_be_write_review_form()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
 
    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "There is no catalogue word in URL"
        
    def should_be_product_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM), "Product form is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET), "Add to basket button is not presented"

    def should_be_write_review_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_WRITE_REVIEW), "Write a review button is not presented"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        add_button.click()

    def should_add_product_to_basket(self):
        url = self.browser.current_url
        self.add_product_to_basket()
        if "promo=" in url:
            self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text 
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert product_name == basket_name, (f"Product name isn't equal to basket name after adding: {product_name} != {basket_name}")
        assert product_cost == basket_cost, (f"Product cost isn't equal to basket cost after adding: {product_cost} != {basket_cost}")

    def should_be_write_review_form(self):
        review_button = self.browser.find_element(*ProductPageLocators.BUTTON_WRITE_REVIEW)
        review_button.click()
        assert self.is_element_present(*ProductPageLocators.REVIEW_FORM), "Review form is not presented"
        assert self.is_element_present(*ProductPageLocators.REVIEW_TITLE), "Review title field is not presented"
        assert self.is_element_present(*ProductPageLocators.REVIEW_SCORE), "Review score field is not presented"
        assert self.is_element_present(*ProductPageLocators.REVIEW_BODY), "Review body field is not presented"
        assert self.is_element_present(*ProductPageLocators.REVIEW_NAME), "Review name field is not presented"
        assert self.is_element_present(*ProductPageLocators.REVIEW_EMAIL), "Review email field is not presented"

    #negative test
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Element is present, when expected not to be!"
        
    #negative test
    def should_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element is present, when expected not to be!"

