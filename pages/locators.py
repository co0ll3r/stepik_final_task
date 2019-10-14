from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # Login fields
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name=login_submit]")
    # Registration fields
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name=registration_submit]") 

class ProductPageLocators():
    # Forms
    PRODUCT_FORM = (By.CSS_SELECTOR, ".product_page") 
    REVIEW_FORM = (By.CSS_SELECTOR, "#addreview") 
    # Product fields
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") 
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color") 
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, ".product_main .availability") 
    PRODUCT_INSTOCK = (By.CSS_SELECTOR, ".product_main .instock") 
    BASKET_NAME = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    BASKET_COST = (By.CSS_SELECTOR, "#messages .alert-info strong")
    # Buttons
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket") 
    BUTTON_WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review") 
    # Review fields
    REVIEW_TITLE = (By.CSS_SELECTOR, "#id_title") 
    REVIEW_SCORE = (By.CSS_SELECTOR, "#id_score") 
    REVIEW_BODY= (By.CSS_SELECTOR, "#id_body") 
    REVIEW_NAME= (By.CSS_SELECTOR, "#id_name") 
    REVIEW_EMAIL = (By.CSS_SELECTOR, "#id_email") 
    # Negative testing fields
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success") 


  
