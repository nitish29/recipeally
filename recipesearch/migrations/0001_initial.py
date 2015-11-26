# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
                ('comment_rating', models.IntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('recipe_text', models.TextField()),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_cuisine', models.CharField(max_length=50)),
                ('recipe_type', models.IntegerField(default=0, choices=[(0, 'Not-Specified'), (1, 'Breakfast'), (2, 'Lunch'), (3, 'Dinner'), (4, 'Snack'), (5, 'Dessert')])),
                ('recipe_picture', models.CharField(max_length=200)),
                ('recipe_calories', models.IntegerField(null=True)),
                ('recipe_prepration_time', models.IntegerField(default=0)),
                ('recipe_serve_people', models.IntegerField(default=0)),
                ('recipe_source', models.CharField(max_length=500)),
                ('ingredient', models.ManyToManyField(to='recipesearch.Ingredients')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_about', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='recipe',
            field=models.ForeignKey(to='recipesearch.Recipes'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
