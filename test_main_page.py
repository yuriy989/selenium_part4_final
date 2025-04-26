import pytest

from .pages.basket_page import BasketPage

from .pages.login_page import LoginPage
from .pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.step_10
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    page = MainPage(browser, LINK)
    page.open()

    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    basket_page = BasketPage(browser, page.browser.current_url)

    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_emty_basket_text()
