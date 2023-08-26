from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.PageObject import PageObject


class SearchPage(PageObject):
    txt_search_page = '//div[@class="page-title"]/h1'
    search_result = '//h2//a'
    product = '//h2[@class="product-title"]//a'

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver=driver)

    def has_search_title(self):
        return self.has_title(self.txt_search_page)

    def validate_search_result(self, expected_result):

        wait = WebDriverWait(self.driver, 10)

        search_result = wait.until(EC.presence_of_element_located((By.XPATH, self.search_result)))
        actual_result = search_result.text

        return expected_result in actual_result

    def open_product(self, product_name):
        product = '//h2[@class="product-title"]//a[contains(text(),"'+product_name+'")]'
        self.driver.find_element(By.XPATH, product).click()

