import math
import time
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException 

class MainPage(BasePage):
    def go_to_login_page(self):
       login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
       login_link.click() 
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

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

