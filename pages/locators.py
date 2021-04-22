from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REVIEW_MY_CART = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")


class LoginPageLocators():
    LOGING_FORM = (By.ID, "login_form")
    SIGNIN_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6 h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6 > .price_color")
    ALERT_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1)")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    NAME_OF_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > div >strong")
    COST_OF_PRODUCT = (By.CSS_SELECTOR, ".row .price_color:nth-child(2)")
    COST_OF_PRODUCT_IN_THE_ALERT = (By.CSS_SELECTOR, ".alert-info strong:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators():
    ALERT_CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner >p")
    CART_ITEMS = (By.CLASS_NAME, "basket-items")


class SignInFormLocators():
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    SIGNIN_CTA = (By.CSS_SELECTOR, "[value='Register']")




