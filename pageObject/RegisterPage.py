from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.PageObject import PageObject


class RegisterPage(PageObject):

    url = 'https://demowebshop.tricentis.com/register'
    gender_female = 'gender-female'
    first_name = 'FirstName'
    last_name = 'LastName'
    email = 'Email'
    password = 'Password'
    confirm_password = 'ConfirmPassword'
    register_button = 'register-button'
    class_register_message = 'result'

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver=driver)

    def click_gender_female(self):
        self.driver.find_element(By.ID, self.gender_female).click()

    def register_new_user(self, first_name="Ana", last_name="Ferreira", email="ana@email.com", password="1234567", confirm_password="1234567"):
        self.click_gender_female()
        self.driver.find_element(By.ID, self.first_name).send_keys(first_name)
        self.driver.find_element(By.ID, self.last_name).send_keys(last_name)
        self.driver.find_element(By.ID, self.email).send_keys(email)
        self.driver.find_element(By.ID, self.password).send_keys(password)
        self.driver.find_element(By.ID, self.confirm_password).send_keys(confirm_password)
        self.click_register_btn()

    def is_url_register(self):
        return self.driver.current_url == self.url

    def click_register_btn(self):
        self.driver.find_element(By.ID, self.register_button).click()

    def validate_register_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_register_message).is_displayed()

