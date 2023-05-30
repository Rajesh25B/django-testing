from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from app1.views import homePage


class SmokeTest(TestCase):
    
    def testHomePageURL(self):
        url = resolve('/home', urlconf=None)
        self.assertEqual(url.func, homePage)
    
    def testTitle(self):
        request = HttpRequest()
        response = homePage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>New Title</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))        


class BrowserSetupTest(TestCase):
    '''manually render the template ourselves in the test'''
    def setUp(self):
        self.response = self.client.get('/home')
        
    def test_return_correct_home_page(self):
        html = self.response.content.decode('utf8')
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_can_save_a_post_request(self):
        response = self.client.post('/home', data={"item_text": "A new list item"})
        self.assertIn('A new list item', response.content.decode())

    def test_templates_to_render_response(self):
        response = self.client.post('/home', data={'item_text': "New Data"})
        self.assertTemplateUsed(self.response, 'home.html')
