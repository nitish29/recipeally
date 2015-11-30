from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
class HomeViewTestCase(TestCase):
	def test_search_url(self):
		resp = self.client.get(reverse('login'))
		self.assertEqual(resp.status_code, 200)

	def test_search(self):
		c=Client()
		response = c.get('/recipe?q=butter+chicken')
		self.assertTrue(b'recipe' in response.content)

	def test_blank(self):
		c=Client()
		response = c.get('/recipe?q=')
		self.assertTrue(b'recipe' in response.content)