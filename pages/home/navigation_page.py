import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "//a[contains(text(),'HOME')]"
    _my_courses = "//a[contains(text(),'MY COURSES')]"
    _all_courses = "//a[contains(text(),'ALL COURSES')]"
    _support = "//a[contains(text(),'SUPPORT')]"
    # _practice = "Practice"
    _user_settings_icon = "//button[@id='dropdownMenu1']"
    # "//span[contains(text(),'My Account')]"

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="xpath")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="xpath")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                                  locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon,
                          locatorType="xpath")
