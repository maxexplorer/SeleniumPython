from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PRODUCT), 'Product in the basket, but should not be'

    def should_be_empty_basket_message(self):
        self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), 'Message basket empty is not presented'
