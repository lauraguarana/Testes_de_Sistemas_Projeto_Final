from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.PageObject import PageObject


class WishlistPage(PageObject):

    url = 'https://demowebshop.tricentis.com/wishlist'
    product_name = 'product'
    wishlist_table = '//table[@class="cart"]'

    def __init__(self, driver):
        super(WishlistPage, self).__init__(driver=driver)

    def check_wishlist_page(self):
        return self.driver.current_url == self.url

    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, self.product_name).text

    def search_element_in_table(self, product_name):
        wait = WebDriverWait(self.driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, self.wishlist_table)))
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            for cell in cells:
                if product_name in cell.text:
                    return True

        return False
