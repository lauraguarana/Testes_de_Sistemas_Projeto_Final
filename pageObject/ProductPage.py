from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.PageObject import PageObject


class ProductPage(PageObject):
    wishlist_btn = 'add-to-wishlist-button-51'
    wishlist_message = '//p[text()="The product has been added to your "]'
    product_name = '//div[@class="product-name"]//h1'

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver=driver)

    def click_add_wishlist_btn(self):
        self.driver.find_element(By.ID, self.wishlist_btn).click()

    def validate_wishlist_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located((By.XPATH, self.wishlist_message)))

    def get_product_name(self):
        name_product = self.driver.find_element(By.XPATH, self.product_name).text
        name_product_trim = name_product.strip()
        return name_product_trim

