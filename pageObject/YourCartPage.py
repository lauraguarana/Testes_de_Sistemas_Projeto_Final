from selenium.webdriver.common.by import By

from pageObject.PageObject import PageObject


class YourCartPage(PageObject):

    url = 'https://demowebshop.tricentis.com/cart'
    remove_product = 'removefromcart'
    qty_field = 'qty-input'
    update_cart_btn = 'updatecart'
    accept_terms = 'terms-of-service'
    checkout_btn = 'checkout-buttons'

    def __init__(self, driver):
        super(YourCartPage, self).__init__(driver=driver)

    def check_cart_page(self):
        return self.driver.current_url == self.url

    def click_checkout(self):
        self.driver.find_element(By.CLASS_NAME, self.accept_terms).is_selected()
        self.driver.find_element(By.CLASS_NAME, self.checkout_btn).click()

    def update_cart(self):
        self.driver.find_element(By.NAME, self.update_cart_btn).click

    def update_prod_qty(self):
        self.driver.find_element(By.CLASS_NAME, self.qty_field).send_keys('3')
        self.driver.find_element(By.NAME, self.update_cart_btn).click