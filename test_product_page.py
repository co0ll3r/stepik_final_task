import pytest
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage

@pytest.mark.skip()
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()

@pytest.mark.skip()
@pytest.mark.parametrize('link', ['0','1','2','3','4','5','6',
                                    pytest.param('7', marks = pytest.mark.xfail),
                                    '8','9'])
def test_guest_should_see_product_promo_offer_pages(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_add_product_to_basket()

@pytest.mark.skip()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()

@pytest.mark.skip()
def test_guest_cant_see_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.skip()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_message_disappear()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = CartPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_basket_be_empty()
    
@pytest.mark.xfail
def test_guest_will_see_product_added_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    page = CartPage(browser, link)
    page.go_to_basket_page()
    page.should_basket_be_empty()
 
