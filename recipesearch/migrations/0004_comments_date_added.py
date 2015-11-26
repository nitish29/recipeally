# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesearch', '0003_remove_comments_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date_added',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
    ]
