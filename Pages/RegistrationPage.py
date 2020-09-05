import time
from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    NAME_FILED = (By.NAME, "name")
    EMAIL_FILED = (By.NAME, "email")
    PASSWORD_FILED = (By.ID, "exampleInputPassword1")
    CHECKBOX = (By.ID, "exampleCheck1")
    SELECT_GENDER = (By.ID, "exampleFormControlSelect1")
    SELECT_RADIO_BUTTON = (By.XPATH, "//input[@type='radio']/..//label")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//strong[.='Success!']")
    PHOTO_COMMERCE_LINK = (By.LINK_TEXT, "ProtoCommerce")
    HOME_LINK = (By.LINK_TEXT, "Home")
    SHOP_LINK = (By.LINK_TEXT, "Shop")
    IMAGE = (By.XPATH, "//div[@class='jumbotron']")

    def verify_title(self, title):
        return self.getTitle(title)

    def enter_name(self):
        try:
            return self.driver.find_element(*RegistrationPage.NAME_FILED)
        except:
            print_stack()

    def enter_email(self):
        return self.driver.find_element(*RegistrationPage.EMAIL_FILED)

    def enter_password(self):

        return self.driver.find_element(*RegistrationPage.PASSWORD_FILED)

    def do_click(self):

        return self.driver.find_element(*RegistrationPage.CHECKBOX)

    def getGender(self):

        return self.driver.find_element(*RegistrationPage.SELECT_GENDER)

    def submitForm(self):
        return self.driver.find_element(*RegistrationPage.SUBMIT_BUTTON)

    def getSuccessMessage(self):
        return self.driver.find_element(*RegistrationPage.SUCCESS_MESSAGE)

    def verify_proto_link(self):
        element = self.driver.find_element(*RegistrationPage.PHOTO_COMMERCE_LINK)
        if element.is_displayed():
            return bool(element)
        else:
            return None

    def verify_home_link(self):
        element = self.driver.find_element(*RegistrationPage.HOME_LINK)
        if element.is_displayed():
            return bool(element)
        else:
            return None

    def verify_shop_link(self):
        element = self.driver.find_element(*RegistrationPage.SHOP_LINK)
        if element.is_displayed():
            return bool(element)
        else:
            return None

    def verify_image(self):
        element = self.driver.find_element(*RegistrationPage.IMAGE)
        if element.is_displayed():
            return bool(element)
        else:
            return None
