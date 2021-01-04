from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.logout()
        self.lp.login("badekarganesh04@gmail.com", "G@nu1992")
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful...!")

    # @pytest.mark.run(order=1)
    # def test_invalidLogin(self):
    #     self.lp.login("badekarganesh04@gmail.com", "G@nu1992222")
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True
