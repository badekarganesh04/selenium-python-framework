import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _search_box = "//input[@id='search']"
    _submit_search = "//button[@type='submit']"
    _course = "//div[@class='zen-course-list']"
    _all_courses = "//a[contains(text(),'ALL COURSES')]"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _submit_enroll = "//body[@class='body-style']/div[@id='page']/div[@id='header19']/" \
                     "div[@class='container']/div[@class='row']/div[@class='checkout-container col-md-8']/" \
                     "div[@id='zen_cs_checkout_dynamic']/div/form[@id='checkout-form']/div[@class='panel']/" \
                     "div[@class='panel payment-panel']/div[@class='panel-body block-zen-space']" \
                     "/div[contains(@class,'stripe-outer')]/" \
                     "div[@class='row']/div[@class='col-xs-12']/button[1]"
    _enroll_error_message = "//div[@class='alert alert-danger']"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType="xpath")
        self.elementClick(self._submit_search, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName), locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        time.sleep(6)
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        # Hint: Call all three methods to enter card details
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num, exp, cvv):
        """
        Hint:
            1. Click on the enroll button
            2. Scroll down
            3. Enter credit card information
            4. Click Enroll in course button
        """
        self.clickEnrollButton()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollBy(0, 700);")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        """
        1. Verify the element for error message is displayed, not just
        present.
        2. You need to verify if it is displayed

        Hint:
        - The element is not instantly displayed, it take some time to display
        - You need to wait for it to display
        """
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
