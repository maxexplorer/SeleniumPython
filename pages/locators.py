from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alert-info .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group')
    BASKET_PRODUCT = (By.CSS_SELECTOR, '.basket-items')
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, 'div#content_inner')


