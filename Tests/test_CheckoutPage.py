from Pages.CheckoutPage import CheckoutPage
from Pages.ShopPage import ShopPage
from Tests.test_Base import BaseTest
from Tests.test_ShopPage import Test_Shop
from configuration.testdata import TestData


class Test_CheckoutPage(BaseTest):

    def test_end_to_end(self):
        sp = ShopPage(self.driver)
        checkout = CheckoutPage(self.driver)
        sp.click_on_shop_link().click()
        sp.add_items_cart(TestData._ITEM)
        sp.click_checkout_button().click()
        sp.verify_items_checkout_page()
        checkout.click_checkout_button_at_checkout_page().click()
        checkout.enter_get_Country(TestData._COUNTRY, TestData._COUNTRY_SELECT)
        assert checkout.get_value() == TestData._COUNTRY_SELECT
        assert checkout.verify_Success_message() in TestData._SUCCESS_MESSAGE
