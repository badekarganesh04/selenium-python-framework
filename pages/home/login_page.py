import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage

import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[contains(text(),'Sign In')]"
    _email_field = "//form[@role='form']//div[@class='form-group']//input[@id='email']"
    _password_field = "password"
    _login_button = "//input[@type='submit']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        # self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']", locatorType="xpath")
        return result

    def logout(self):
        self.nav.navigateToUserSettings()
        self.elementClick(locator="//a[contains(text(),'Logout')]",
                          locatorType="xpath")

    # def verifyLoginFailed(self):
    #     # time.sleep(3)
    #     result = self.isElementPresent(
    #         "//div/span[contains(text(), 'Your username or password is invalid. Please try again.')]",
    #         locatorType="xpath")
    #     return result

    # def clearFields(self):
    #     emailField = self.getElement(locator=self._email_field)
    #     emailField.clear()
    #     passwordField = self.getElement(locator=self._password_field)
    #     passwordField.clear()
