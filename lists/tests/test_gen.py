
from django.test import TestCase
from lists.views import main_page

class GenTest(TestCase):

    def test_response(self):

        response = self.client.get('/main/')
        html = response.content.decode('utf8')
#         from django.http import HttpRequest
#         request = HttpRequest()
#         response = main_page(request)
#         import pdb;pdb.set_trace()
        self.assertTrue(html.startswith('<html>'))
        
        self.assertIn('h1', html)

        return response.content

    def test_template(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')

        
        self.assertIn('<html>', html)
        self.assertIn('h1', html)
        
        self.assertTemplateUsed(response, 'root_page.html')
        return None