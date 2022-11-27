import pytest
from pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize('link', [f"{product_base_link}/?promo=offer0",
                                  f"{product_base_link}/?promo=offer1",
                                  f"{product_base_link}/?promo=offer2",
                                  f"{product_base_link}/?promo=offer3",
                                  f"{product_base_link}/?promo=offer4",
                                  f"{product_base_link}/?promo=offer5",
                                  f"{product_base_link}/?promo=offer6",
                                  pytest.param(f"{product_base_link}/?promo=offer7", marks=pytest.mark.xfail),
                                  f"{product_base_link}/?promo=offer8",
                                  f"{product_base_link}/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_contains_correct_product_name()
    page.message_contains_correct_total_cost()
