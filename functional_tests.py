import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestNewMember(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testMember(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn(
            "New Title",
            self.browser.title
        )
        # self.fail('Test is failing...')


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''helper function to check items in a table'''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_basic_html_page_features(self):
        self.browser.get('http://localhost:8000/')

        # test title
        self.assertEqual('New Title', self.browser.title)

        # test header tag
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('This is H1 tag', header_text)

        # test input element value
        inputbox = self.browser.find_element(By.ID, "input1")
        # test placeholder value
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter your name'
        )

        # test input value typed
        inputbox.send_keys('1: Complete unittest')
        inputbox.send_keys('2: Complete TDD')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Test the items in the table basic way

        # table = self.browser.find_element(By.TAG_NAME, "table")
        # rows = table.find_elements(By.TAG_NAME, 'tr')

        # self.assertIn('1: Complete unittest', [row.text for row in rows])
        # self.assertIn(
        #     '2: Complete TDD',
        #     [row.text for row in rows]
        # )
        
        # Test multiple items in the table using helper method
        # follow DRY principle
        # This test failed becoz there is no way to store the items without database
        
        self.check_for_row_in_list_table('1: Complete unittest')
        self.check_for_row_in_list_table('2: Complete TDD')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # launches the unittest test runner which will automatically find test
    # classes and methods in the file and run them.
