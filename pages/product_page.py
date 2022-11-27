from decimal import Decimal
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.constants import TIMEOUT


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=TIMEOUT):
        super().__init__(browser, url, timeout)
        self.name = None
        self.price = 0
        self.basket_total = 0

    def open(self):
        super().open()
        self.name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.price = self.get_cost(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)

    def add_to_basket(self):
        self.check_product_availability()
        self.basket_total = self.get_cost(self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text)
        add_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET)
        add_basket.click()

    def message_contains_correct_product_name(self):
        self.message_adding_product_is_presented()
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text == self.name, \
            "Product names don't match"

    def message_contains_correct_total_cost(self):
        self.message_your_basket_total_is_presented()
        expected_basket_total = self.basket_total + self.price
        current_basket_total = self.get_cost(
            self.browser.find_element(*ProductPageLocators.MESSAGE_YOUR_BASKET_TOTAL).text
        )
        assert expected_basket_total == current_basket_total, \
            f"Current basket total ({current_basket_total}) doesn't match the expected ({expected_basket_total})"

    def check_product_availability(self):
        assert "In stock" in self.browser.find_element(*ProductPageLocators.AVAILABILITY).text, \
            "Product is out of stock"

    def message_adding_product_is_presented(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDING), \
            "Message about adding the product is not presented"

    def message_your_basket_total_is_presented(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_YOUR_BASKET), \
            "Message about your basket total is not presented"

    @staticmethod
    def get_cost(raw_string: str):
        number_string = "".join(filter(lambda s: s in "0123456789.", raw_string))
        return Decimal(number_string.strip('.'))
