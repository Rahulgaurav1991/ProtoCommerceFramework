import time

import pytest

from Pages.BasePage import BasePage
from Pages.RegistrationPage import RegistrationPage
from Tests.test_Base import BaseTest
from configuration.testdata import TestData


class Test_registration(BaseTest):
    text = None

    def test_verify_title(self):
        rp = RegistrationPage(self.driver)
        assert rp.verify_title(TestData._TITLE) == TestData._TITLE, " title is matching "

    def test_verify_links(self):
        rp = RegistrationPage(self.driver)
        rp.verify_proto_link()
        rp.verify_home_link()
        rp.verify_shop_link()
        rp.verify_image()

    def test_verify_Registration_Page(self):
        rp = RegistrationPage(self.driver)
        rp.enter_name().send_keys(TestData._NAME)
        rp.enter_email().send_keys(TestData._EMAIL)
        rp.enter_password().send_keys(TestData._PASSWORD)
        rp.do_click().click()
        #self.select_by_text(rp.getGender(), TestData._GENDER)
        rp.submitForm().click()
        text = rp.getSuccessMessage().text.lstrip()
        assert text == TestData._MESSAGE
