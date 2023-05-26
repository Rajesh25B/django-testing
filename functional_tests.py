import unittest
from selenium import webdriver


class TestNewMember(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testMember(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('New Title', self.browser.title)
        self.fail('Done testing')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # launches the unittest test runner which will automatically find test
    # classes and methods in the file and run them.
