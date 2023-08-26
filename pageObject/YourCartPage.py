from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from faker import Faker
from pageObject.PageObject import PageObject


class YourCartPage(PageObject):

    url = 'https://demowebshop.tricentis.com/cart'
    remove_product = 'removefromcart'
    qty_field = 'qty-input'
    update_cart_btn = 'updatecart'
    accept_terms = 'termsofservice'
    checkout_btn = 'checkout-buttons'
    cart_prod_qty = 0

    fake = Faker()

    def __init__(self, driver):
        super(YourCartPage, self).__init__(driver=driver)

    def check_cart_page(self):
        return self.driver.current_url == self.url

    def click_checkout(self):
        self.driver.find_element(By.ID, self.accept_terms).click()
        self.driver.find_element(By.CLASS_NAME, self.checkout_btn).click()

    def update_prod_qty(self):
        faker = self.fake.random_digit()
        self.driver.find_element(By.CLASS_NAME, self.qty_field).clear()
        self.driver.find_element(By.CLASS_NAME, self.qty_field).send_keys(faker)
        self.driver.find_element(By.CLASS_NAME, self.qty_field).send_keys(Keys.ENTER)
        self.driver.find_element(By.NAME, self.update_cart_btn).click()

    def remove_prod(self):
        self.driver.find_element(By.NAME, self.remove_product).click()
        self.driver.find_element(By.NAME, self.update_cart_btn).click()

    def get_quantity(self):
        cart_prod_qty = self.driver.find_element(By.CLASS_NAME, self.qty_field).get_attribute('value')

    def compare_qty(self):
        cart_new_qty = self.driver.find_element(By.CLASS_NAME, self.qty_field).get_attribute('value')
        if self.cart_prod_qty != cart_new_qty:
            return True

        return False

