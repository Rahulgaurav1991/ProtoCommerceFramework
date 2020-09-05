"""this is the parent of all the pages """
from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of(by_locator)).click()

        except:
            print_stack()

    def send_value(self, by_locator):
        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of(by_locator))

        except:
            print_stack()

    def getTitle(self, title):
        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.title_is(title))
            return self.driver.title

        except:
            print_stack()

    def select_value(self, by_locator, value):

        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of(by_locator))
            Select(by_locator).select_by_value(value)
        except:
            print_stack()

    def select_by_text(self, locator, text):

        sel = Select(locator)
        sel.select_by_visible_text(text)

    def select_radio_button(self, by_locator, value):
        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of(by_locator))
            items = self.driver.find_elements(by_locator)
            for item in items:
                text = item.text
                if text == value:
                    break

                else:
                    print("no values are available")

        except:
            print_stack()

    def is_visibility_element(self, by_locator):
        element = WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of(by_locator))
        return bool(element)

    def scroll_Page(self, element):

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
