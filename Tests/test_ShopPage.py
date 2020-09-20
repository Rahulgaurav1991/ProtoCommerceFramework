import time

from Pages.CheckoutPage import CheckoutPage
from Pages.ShopPage import ShopPage
from Tests.test_Base import BaseTest
from configuration.testdata import TestData


class Test_Shop(BaseTest):
    title = None

    def test_verify_shop_link(self):
        sp = ShopPage(self.driver)
        sp.click_on_shop_link().click()
        title = sp.verify_title(TestData._TITLE)
        assert title == TestData._TITLE

    def test_verify_items(self):
        sp = ShopPage(self.driver)
        sp.click_on_shop_link().click()
        assert sp.verify_items() == TestData._LIST_ITEMS

    def test_add_items_and_verify(self):
        sp = ShopPage(self.driver)
        sp.click_on_shop_link().click()
        item_from_shop_page = sp.add_items_cart(TestData._ITEM)  # adding items as per requirments
        sp.click_checkout_button().click()
        item_from_checkout_page = sp.verify_items_checkout_page()  # getting items from Checkout page
        assert item_from_shop_page == item_from_checkout_page



