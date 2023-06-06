import unittest

from selenium import webdriver
from django.test import LiveServerTestCase


class TestNewMember(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testMember(self):
        self.browser.get(LiveServerTestCase.live_server_url)
        self.assertIn('New Title', self.browser.title)
        self.fail('Done testing')


# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
    # launches the unittest test runner which will automatically find test
    # classes and methods in the file and run them.
