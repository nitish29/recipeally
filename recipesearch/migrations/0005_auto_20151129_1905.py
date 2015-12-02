# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesearch', '0004_comments_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_rating',
            field=models.IntegerField(null=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
