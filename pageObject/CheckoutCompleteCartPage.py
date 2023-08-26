from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.PageObject import PageObject


class CheckoutCompleteCartPage(PageObject):
    url = 'https://demowebshop.tricentis.com/checkout/completed/'
    text_title_page = 'Thank you'
    thank_you_message = '//div[@class="title"]//strong'
    text_thank_you_message = 'Your order has been successfully processed!'

    def __init__(self, driver):
        super(CheckoutCompleteCartPage, self).__init__(driver=driver)

    def check_checkout_complete_page(self):
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.url))

    def check_thank_message(self):
        return self.driver.find_element(By.XPATH, self.thank_you_message).text == self.text_thank_you_message