from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.PageObject import PageObject


class HomePage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    register_button = 'ico-register'
    login_button = 'ico-login'
    wishlist_button = 'ico-wishlist'
    shopping_cart_button = 'ico-cart'
    search_bar = 'search-box-text ui-autocomplete-input'
    search_button = 'button-1 search-box-button'
    add_product = '(//input[@value="Add to cart"])[2]'
    bar_notification = 'bar-notification'
    cart_qty = '//span[@class="cart-qty"]'

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def click_register_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.register_button).click()

    def click_login_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button).click()

    def click_wishlist_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.wishlist_button).click()

    def click_shopping_cart_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.shopping_cart_button).send_keys(Keys.PAGE_UP)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, self.shopping_cart_button)))
        self.driver.find_element(By.CLASS_NAME, self.shopping_cart_button).click()

    def click_search_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.search_button).click()

    def search_product(self, productname):
        self.driver.find_element(By.CLASS_NAME, self.search_bar).send_keys(productname)
        self.click_search_btn()

    def add_product_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_product).click()

    def verify_bar_notification(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located((By.ID, self.bar_notification)))

    def verify_shopping_cart_qty(self):
        cart_prod_qty = self.driver.find_element(By.XPATH, self.cart_qty).text
        if cart_prod_qty != '(0)':
            self.driver.find_element(By.CLASS_NAME, self.shopping_cart_button).click()
        else:
            self.add_product_to_cart()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.CLASS_NAME, self.shopping_cart_button).send_keys(Keys.PAGE_UP)
            self.driver.find_element(By.CLASS_NAME, self.shopping_cart_button).click()