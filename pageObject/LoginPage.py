from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.PageObject import PageObject

class LoginPage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    email_field = 'Email'
    password_field = 'Password'
    log_in_button = '//input[@value="Log in"]'
    logout_button = 'ico-logout'
    url_login = 'https: // demowebshop.tricentis.com / login'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver=driver)

    def input_login(self):
        self.driver.find_element(By.ID, self.email_field).send_keys('joao@joao.com')
        self.driver.find_element(By.ID, self.password_field).send_keys('123456')

    def click_log_in_btn(self):
        self.driver.find_element(By.XPATH, self.log_in_button).click()

    def verify_login(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, self.logout_button)))

    def is_url_login(self):
        return self.driver.current_url != self.url_login