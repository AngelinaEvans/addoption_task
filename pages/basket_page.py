from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def check_the_alert_cart_is_empty(self):
        empty_cart_alert = self.browser.find_element(*CartPageLocators.ALERT_CART_IS_EMPTY)
        assert "Your basket is empty" in empty_cart_alert.text, "Your basket is empty message is not showing"

    def check_the_cart_items_not_displayed(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "The basket contains the product items. " \
																"But should be empty"

