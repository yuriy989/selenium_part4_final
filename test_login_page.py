from .pages.login_page import LoginPage


link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
