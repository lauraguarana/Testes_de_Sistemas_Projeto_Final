from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.PageObject import PageObject


class YourCartPage(PageObject):

    url = 'https://demowebshop.tricentis.com/cart'
    remove_product = 'removefromcart'
    qty_field = 'qty-input'
    update_cart_btn = 'updatecart'
    accept_terms = 'termsofservice'
    checkout_btn = 'checkout-buttons'
    empty_cart_msg = 'order-summary-content'

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
       return cart_prod_qty
    def get_new_qty(self):
        cart_new_qty = self.driver.find_element(By.CLASS_NAME, self.qty_field).get_attribute('value')
        return cart_new_qty
    def compare_qty(self):
        old_qty = self.get_quantity()
        print(old_qty)
        new_qty = self.get_new_qty()
        print(new_qty)



    def validate_empty_cart(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, self.empty_cart_msg)))