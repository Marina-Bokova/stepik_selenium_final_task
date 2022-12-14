from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # Initialize the Page Object, pass the driver instance and url to the constructor
    page.open()  # Open the page
    page.go_to_login_page()  # Execute the page method - go to the login page
    login_page = LoginPage(browser, browser.current_url)  # Initialize the Page Object for LoginPage
    login_page.login_page_is_valid()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.login_link_is_presented()
