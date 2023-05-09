from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def add_to_basket_successful(self):
        messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        self.should_be_message_add_to_basket(messages[0].text)
        self.should_be_message_total_basket_price(messages[2].text)

    def should_be_message_add_to_basket(self, name):
        assert name == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, \
            "Product name not match"

    def should_be_message_total_basket_price(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, \
            "Total price not match"
