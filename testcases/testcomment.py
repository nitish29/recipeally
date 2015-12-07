from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from recipesearch.models import Comments
class HomeViewTestCase(TestCase):

	# def test_comment(self):
	# 	c=Client()
	# 	response = c.get('/recipe?q=butter+chicken')
	# 	self.assertTrue(b'comment' in response.content)

	# def test_comment_blank(self):
	# 	c=Client()
	# 	response = c.post('/recipe?q=butter+chicken', {'comment_text': ''})
	# 	self.assertTrue(b'This field is required.' in response.content)

	# def test_comment_valid(self):
	# 	c=Client()
	# 	response = c.post('/recipe?q=butter+chicken', {'comment_text': 'test_hello'})
	# 	comm=Comments.objects.get(comment_text="test_hello")
	# 	print(comm)
	# 	self.assertTrue('test_hello' in comm.comment_text)