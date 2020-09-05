import time
from traceback import print_stack

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ShopPage(BasePage):
    text = None

    def __init__(self, driver):
        super().__init__(driver)

    SHOP_LINK = (By.LINK_TEXT, "Shop")
    BUTTON_LINK = (By.CSS_SELECTOR, "button[class='btn btn-info']")
    CART_ITEMS = (By.XPATH, "//div[@class='card-body']//h4")
    VERIFY_CHECKOUT_ICON = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    IPHONE_BUTTON = (By.XPATH, " //a[.='iphone X']/../../..//button")
    SAMSUNG_BUTTON = (By.XPATH, " //a[.='Samsung Note 8']/../../..//button")
    NOKIA_BUTTON = (By.XPATH, " //a[.='Nokia Edge']/../../..//button")
    BLACKBERRY_BUTTON = (By.XPATH, " //a[.='Blackberry']/../../..//button")
    ITEMS_AT_CHECKOUT_PAGE = (By.XPATH, "//table//td//h4//a")

    def click_on_shop_link(self):
        return self.driver.find_element(*ShopPage.SHOP_LINK)

    def verify_title(self, title):
        return self.getTitle(title)

    def verify_items(self):
        text = None
        list = []
        # self.scroll_Page(self.BUTTON_LINK)
        try:
            element = self.driver.find_elements(*ShopPage.CART_ITEMS)
            if len(element) > 0:
                for items in element:
                    list.append(items.text)
            print("the items in list are ---->" + str(list))
            return list
        except:
            print_stack()

    def verify_size_checkout_icon(self):
        size = self.driver.find_element(*ShopPage.VERIFY_CHECKOUT_ICON)
        if len(size) > 0:
            return True
        else:
            return False

    def add_items_cart(self, value):  # for Adding single Products
        element = self.driver.find_elements(*ShopPage.CART_ITEMS)
        for items in element:
            text = items.text
            if text == value:
                self.driver.find_element(*ShopPage.IPHONE_BUTTON).click()
                print("the items selected is:-->" + text)
                return text
            elif text == value:
                self.driver.find_element(*ShopPage.SAMSUNG_BUTTON).click()
                print("the items selected is:-->" + text)
                # self.verify_size_checkout_icon()
                return text
            elif text == value:
                self.driver.find_element(*ShopPage.NOKIA_BUTTON).click()
                self.verify_size_checkout_icon()
                print("the items selected is:-->" + text)
                return text

            elif text == value:
                self.driver.find_element(*ShopPage.BLACKBERRY_BUTTON).click()
                # self.verify_size_checkout_icon()
                print("the text is:-->" + text)
                return text

            else:
                print("No items in cart")

    def click_checkout_button(self):
        return self.driver.find_element(*ShopPage.VERIFY_CHECKOUT_ICON)

    def verify_items_checkout_page(self):
        all_items = self.driver.find_elements(*ShopPage.ITEMS_AT_CHECKOUT_PAGE)
        for items in all_items:
            print("the items at checkoutpage is:---->" + items.text)
            return items.text
