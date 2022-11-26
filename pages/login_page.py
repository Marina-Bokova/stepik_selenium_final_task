from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login_page_is_valid(self):
        self.url_contains_login_str()
        self.login_form_is_presented()
        self.register_form_is_presented()

    def url_contains_login_str(self):
        url_page = self.browser.current_url
        assert "login" in url_page, \
            "Failed to go to login page"

    def login_form_is_presented(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def register_form_is_presented(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"
