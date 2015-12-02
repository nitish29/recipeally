from django.core.urlresolvers import reverse
from django.test import TestCase
from recipesearch.models import UserProfile
from django.contrib.auth.models import User
from django.test import Client
class LoginViewTestCase(TestCase):
	def test_login_url(self):
		resp = self.client.get(reverse('login'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('user'in resp.context)
	
	def test_login_both_invalid(self):
		c=Client()
		response = c.post('/login/', {'username': 'john', 'password': 'smith'})
		self.assertTrue(b'Invalid login details' in response.content)
	
	def test_login_password_invalid(self):
		c=Client()
		u=User.objects.create_user(username='archit',password='123')
		u.save()
		response = c.post('/login/', {'username': 'archit', 'password': 'abc'})
		self.assertTrue(b'Invalid login details' in response.content)

	def test_login_success(self):
		c=Client()
		u=User.objects.create_user(username='archit',password='123')
		u.save()
		entries = User.objects.all()
		response = c.post('/login/', {'username': 'archit', 'password': '123'})
		self.assertFalse(b'Invalid login details' in response.content)