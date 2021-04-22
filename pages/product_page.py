from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
	def add_product_to_the_cart_with_quiz(self):
		add_to_cart_btn = WebDriverWait(self.browser, 5).until(
			EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CARD_BUTTON))
		add_to_cart_btn.click()
		self.solve_quiz_and_get_code()

	def add_product_to_the_cart_without_quiz(self):
		add_to_cart_btn = WebDriverWait(self.browser, 5).until(
			EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CARD_BUTTON))
		add_to_cart_btn.click()

	def check_product_added(self):
		alert_product_added = WebDriverWait(self.browser, 5).until(
			EC.visibility_of_element_located(ProductPageLocators.ALERT_PRODUCT_ADDED))
		assert alert_product_added.is_displayed()

	def check_the_added_product_name(self):
		name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
		name_of_product.text
		name_of_added_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_ALERT)
		name_of_added_product.text
		assert name_of_product.text == name_of_added_product.text

	def check_the_added_product_price(self):
		cost_of_product = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT)
		cost_of_product.text
		cost_of_added_product = WebDriverWait(self.browser, 5).until(
			EC.visibility_of_element_located(ProductPageLocators.COST_OF_PRODUCT_IN_THE_ALERT))
		cost_of_added_product.text
		assert cost_of_product.text == cost_of_added_product.text, "The cost of product does not meet to real cost"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED), \
			"Success message is presented, but should not be"

	def should_be_disappeared_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_ADDED), \
			"Success message is disappeared"