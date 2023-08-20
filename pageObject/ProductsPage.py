import time
from random import randint

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObject.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'
    txt_products_title = 'Products'
    class_product_item = 'inventory_item'
    id_menu_btn = "react-burger-menu-btn"
    class_product_card = 'inventory_item'
    class_add_to_cart_btn = 'btn_primary'
    class_cart_badge = 'shopping_cart_badge'
    class_cart_btn = 'shopping_cart_link'
    class_product_name = 'inventory_item_name'
    class_remove_btn = 'btn_secondary'
    text_remove_btn = 'Remove'
    text_add_to_cart_btn = 'Add to cart'
    css_filter_select = '[data-test="product_sort_container"]'
    css_filter_price_low_to_high = '[value="lohi"]'
    class_item_price = '[class="inventory_item_price"]'
    value_low_high = 'lohi'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.is_url(self.url)

    def has_products_title(self):
        return self.has_title(self.txt_products_title)

    def check_products_page(self):
        return self.check_page(self.url, self.txt_products_title)

    def validate_products_in_page(self):
        products_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        return len(products_list) == 6

    def has_menu_button(self):
        try:
            return self.driver.find_element(By.ID, self.id_menu_btn).is_displayed()
        except NoSuchElementException:
            return False


    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_cart_btn).click()


