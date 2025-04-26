from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "/basket/" in self.browser.current_url, "Basket page url is invalid"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), (
            "Basket is not empty"
        )

    def should_be_emty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), (
            "There is no basket empty text"
        )
