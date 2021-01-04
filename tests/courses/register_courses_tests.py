from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        """
        1. Call required methods from the page class to perform the test
        2. Enter course name
        3. Select course
        4. Enroll in course
        5. Verify error message
        6. Test Status.markFinal()
        """
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse("5241810401821657", "1123", "123")
        time.sleep(5)
        result2 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_verifyEnrollment", result2, "Enrollment failed...!")
