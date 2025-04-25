from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_button.click()

    def should_not_shown_success_message(self):
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_MESSAGES)

    def should_disappear_success_message(self):
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS_MESSAGES)

    def get_alert_messages(self):
        alert_messages = []
        for i in self.browser.find_elements(
            *ProductPageLocators.ALERT_SUCCESS_MESSAGES
        ):
            alert_messages.append(i.text)

        return alert_messages

    def should_be_same_price_in_messages(self):
        in_description = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        in_message = self.browser.find_element(
            *ProductPageLocators.PRICE_IN_MESSAGE
        ).text
        assert in_description == in_message, (
            "Basket total in message is not equal to product price"
        )

    def should_be_same_product_name_in_messages(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Проверяем во всех сообщениях чтобы не зависеть от языка и их порядка
        assert product_name in self.get_alert_messages(), (
            "Message has different product name or not present"
        )
