from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # Initialize the Page Object, pass the driver instance and url to the constructor
    page.open()                     # Open the page
    page.go_to_login_page()         # Execute the page method - go to the login page

