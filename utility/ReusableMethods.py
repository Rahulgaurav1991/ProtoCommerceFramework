from traceback import print_stack

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Generic:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by_locator, text):

        try:
            WebDriverWait(self.driver, 120).until(
                expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

        except:
            print_stack()

    def wait_for_element_display(self, by_locator):
        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.presence_of_all_elements_located(by_locator))

        except:
            print_stack()

    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of_element_located(by_locator)).click()

        except:
            print_stack()

    def get_text(self, by_locator):
        try:
            Text = WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of_element_located(by_locator)).text
            return Text

        except:
            return None

            print_stack()
