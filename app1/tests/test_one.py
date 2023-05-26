from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from app1.views import homePage


class SmokeTest(TestCase):
    
    def testHomePageURL(self):
        url = resolve('/', urlconf=None)
        self.assertEqual(url.func, homePage)
    
    def testTitle(self):
        request = HttpRequest()
        response = homePage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>New Title</title>', html)
        self.assertTrue(html.endswith('</html>'))        


class BrowserSetupTest(TestCase):
    '''manually render the template ourselves in the test'''
    def setUp(self):
        self.response = self.client.get('/')
        
    def test_return_correct_home_page(self):
        html = self.response.content.decode('utf8')
        self.assertTemplateUsed(self.response, 'index.html')
