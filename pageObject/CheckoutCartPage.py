from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.PageObject import PageObject


class CheckoutCartPage(PageObject):
    url = 'https://demowebshop.tricentis.com/onepagecheckout'
    billing_address_continue_btn = '#billing-buttons-container > input'
    shipping_address_continue_btn = '#shipping-buttons-container > input'
    shipping_method_continue_btn = '#shipping-method-buttons-container > input'
    payment_method_continue_btn = '#payment-method-buttons-container > input'
    payment_information_continue_btn = '#payment-info-buttons-container > input'
    confirm_order_btn = '#confirm-order-buttons-container > input'

    def __init__(self, driver):
        super(CheckoutCartPage, self).__init__(driver=driver)

    def check_checkout_cart_page(self):
        return self.driver.current_url == self.url

    def billing_address(self):
        self.driver.find_element(By.CSS_SELECTOR, self.billing_address_continue_btn).click()

    def shipping_address(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, self.shipping_address_continue_btn).click()

    def shipping_method(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, self.shipping_method_continue_btn).click()

    def payment_method(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, self.payment_method_continue_btn).click()

    def payment_information(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, self.payment_information_continue_btn).click()

    def confirm_order(self):
        self.driver.find_element(By.CSS_SELECTOR, self.confirm_order_btn).click()
