from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredients(models.Model):
	ingredient_name = models.CharField(max_length=100)

class Recipes(models.Model):
	recipe_text = models.TextField()
	recipe_name = models.CharField(max_length=100)
	recipe_cuisine = models.CharField(max_length=50, null=True)

	RECIPE_TYPE = (
			(0, 'Not-Specified'),
			(1,'Breakfast'),
			(2, 'Lunch'),
			(3, 'Dinner'),
			(4, 'Snack'),
			(5, 'Dessert'),
		)

	recipe_type = models.IntegerField(default=0, choices=RECIPE_TYPE, null=True)
	recipe_prepration_time = models.IntegerField(default=0, null=True)
	recipe_serve_people = models.IntegerField(default=0, null=True)
	user = models.ForeignKey(User)
	ingredient = models.ManyToManyField(Ingredients)


#TODO : Make a signal function = post_save(), that saves the about data in the user profile table once a new user registers / or an exisitng user updates info

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	user_about = models.CharField(max_length=200, null=True)

class Comments(models.Model):
	comment_text = models.CharField(max_length=200)

	RATING = (
			(0,0),
			(1,1),
			(2,2),
			(3,3),
			(4,4),
			(5,5),
		)

	comment_rating = models.IntegerField(default=0, choices=RATING, null=True)
	recipe_str = models.CharField(default="0",max_length=200)
	user = models.ForeignKey(User)
	date_added = models.DateTimeField(auto_now_add=True, editable=False, null=True)



	



	



