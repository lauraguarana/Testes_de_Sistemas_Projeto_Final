from selenium.webdriver.common.by import By

from pageObject.PageObject import PageObject


class HomePage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    register_button = 'ico-register'
    login_button = 'ico-login'
    wishlist_button = 'ico-wishlist'
    shopping_cart_button = 'ico-cart'
    search_bar = 'search-box-text ui-autocomplete-input'
    search_button = 'button-1 search-box-button'

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def click_register_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.register_button).click()

    """def is_url_login(self):
        return self.driver.current_url == self.url"""

    def click_login_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button).click()

    def click_wishlist_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.wishlist_button).click()

    def click_shopping_cart_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.shopping_cart_button).click()

    def click_search_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.search_button).click()

    def search_product(self, productname):
        self.driver.find_element(By.CLASS_NAME, self.search_bar).send_keys(productname)
        self.click_search_btn()



