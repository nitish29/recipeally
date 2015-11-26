# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesearch', '0002_comments_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date_added',
        ),
    ]
