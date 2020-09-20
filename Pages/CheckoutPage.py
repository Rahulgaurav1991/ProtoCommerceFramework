from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage
from utility.ReusableMethods import Generic


class CheckoutPage(Generic):
    text = None

    def __init__(self, driver):
        super().__init__(driver)

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "input[value='Purchase']")
    PURCHASE_TEXT = (By.ID, "country")
    COUNTRY_LIST = (By.XPATH, "//div[@class='suggestions']//li//a")
    SUCCESS_TEXT = (By.XPATH, " //div[contains(@class,'alert alert-success alert-dismissible')]")

    def click_checkout_button_at_checkout_page(self):
        return self.driver.find_element(*CheckoutPage.CHECKOUT_BUTTON)

    def enter_Purchase_field(self):
        return self.driver.find_element(*CheckoutPage.PURCHASE_TEXT)

    def enter_get_Country(self, text, value):
        self.enter_text(self.PURCHASE_TEXT, text)
        self.wait_for_element_display(self.COUNTRY_LIST)

        countries = self.driver.find_elements(*CheckoutPage.COUNTRY_LIST)
        for country in countries:
            text = country.text
            # print("the country are:--->"+text)

            if text == value:
                country.click()
                print("the selected country is --->" + text)
                return text
            else:
                return None

    def get_value(self):
        return self.driver.find_element(*CheckoutPage.PURCHASE_TEXT).get_attribute("value")

    def verify_Success_message(self):
        self.click(self.PURCHASE_BUTTON)
        value = self.get_text(self.SUCCESS_TEXT)
        s = value.split()
        return s[1]
