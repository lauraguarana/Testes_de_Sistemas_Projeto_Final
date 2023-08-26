from selenium.webdriver.common.by import By

from pageObject.PageObject import PageObject


class WishlistPage(PageObject):

    url = 'https://demowebshop.tricentis.com/wishlist'
    product_name = 'product'

    def __init__(self, driver):
        super(WishlistPage, self).__init__(driver=driver)

    def check_wishlist_page(self):
        return self.driver.current_url == self.url

    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, self.product_name).text

    def verify_number_of_rows(self):
        table = self.driver.find_element_by_css_selector("table.wishlist-table")
        rows = table.find_elements_by_tag_name("tr")
        return len(rows) - 1

    def search_element_on_table(self, nome_produto):
        element = self.driver.find_element_by_xpath(f"//a[text()='{nome_produto}']")
        return element is not None

    def verify_product_added(self, product):
        return self.driver
        self.driver.find_element(By.CSS_SELECTOR, self.css_finish_btn).click()
