import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.step_4
@pytest.mark.parametrize(
    "num",
    [*[i for i in range(1, 10) if i != 7], pytest.param(7, marks=pytest.mark.xfail)],
)
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_same_price_in_messages()
    page.should_be_same_product_name_in_messages()


@pytest.mark.step_6
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()

    page.should_not_shown_success_message()


@pytest.mark.step_6
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()

    page.should_not_shown_success_message()


@pytest.mark.step_6
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()

    page.should_disappear_success_message()


@pytest.mark.step_8
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.step_8
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    LoginPage(browser, page.browser.current_url).should_be_login_page()


@pytest.mark.step_10
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    page = ProductPage(browser, LINK)
    page.open()

    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    basket_page = BasketPage(browser, page.browser.current_url)

    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_emty_basket_text()
