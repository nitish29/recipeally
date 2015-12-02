from django.core.urlresolvers import reverse
from django.test import TestCase
from recipesearch.models import UserProfile
from django.contrib.auth.models import User
from django.test import Client
class LoginViewTestCase(TestCase):
	def test_registration_url(self):
		resp = self.client.get(reverse('registration'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('user'in resp.context)
	
	def test_reg_blank(self):
		c=Client()
		response = c.post('/registration/', {'username': '', 'password': ''})
		self.assertTrue(b'This field is required.' in response.content)
	
	def test_registrations_password_invalid(self):
		c=Client()
		u=User.objects.create_user(username='archit',password='123',email='archit017@gmail.com')
		u.save()
		response = c.post('/registration/', {'username': 'archit', 'password': 'abc','email':'architve@buffalo.edu'})
		self.assertTrue(b'A user with that username already exists.' in response.content)

	def test_registration_success(self):
		c=Client()
		entries = User.objects.all()
		response = c.post('/registration/', {'username': 'archit', 'password': '123','email':'architve@buffalo.edu'})
		self.assertFalse(b'Invalid login details' in response.content)
		self.assertFalse(b'A user with that username already exists.' in response.content)