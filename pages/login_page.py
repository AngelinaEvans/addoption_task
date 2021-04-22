import time

from .base_page import BasePage
from .locators import LoginPageLocators, SignInFormLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, f"/login/ is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGING_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGNIN_FORM), "Sign in Form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*SignInFormLocators.REGISTRATION_EMAIL)
        email_field.send_keys(str(time.time()) + email)
        password_field1 = self.browser.find_element(*SignInFormLocators.REGISTRATION_PASSWORD1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*SignInFormLocators.REGISTRATION_PASSWORD2)
        password_field2.send_keys(password)
        sign_in_cta = self.browser.find_element(*SignInFormLocators.SIGNIN_CTA)
        sign_in_cta.click()




