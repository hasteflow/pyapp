import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def wait_for(self, fn):
        """
        Wait function for selenium driver.
        """
        start_time = time.time()

        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:

                if time.time() - start_time > MAX_WAIT:
                    raise e

                time.sleep(0.5)

    def test_user_can_login_into_application(self):
        self.browser.get("http://localhost:8000/login/")
        time.sleep(3)
        self.browser.find_element("name", "username").send_keys("qwerty_test_user")
        time.sleep(3)
        self.browser.find_element("name", "password").send_keys("12345678aaa")
        time.sleep(3)
        self.browser.find_element("name", "login_button").send_keys(Keys.ENTER)
        time.sleep(3)

        element = self.wait_for(lambda: self.browser.find_element("name", "homepage_greeting"))
        self.assertIn("You are logged in", element.text)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
