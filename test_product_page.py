import pytest

from .pages.product_page import ProductPage


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
