# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesearch', '0005_auto_20151129_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='recipe_calories',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='recipe_picture',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='recipe_source',
        ),
        migrations.AddField(
            model_name='comments',
            name='recipe_str',
            field=models.CharField(max_length=200, default='0'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_cuisine',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_prepration_time',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_serve_people',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_type',
            field=models.IntegerField(default=0, null=True, choices=[(0, 'Not-Specified'), (1, 'Breakfast'), (2, 'Lunch'), (3, 'Dinner'), (4, 'Snack'), (5, 'Dessert')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_about',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
