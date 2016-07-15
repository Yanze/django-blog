# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_link',
            field=models.CharField(default='http://f.tqn.com/y/cats/1/S/i/O/4/AngryCat98125846-Barbara-Singer2040x1471.jpg', max_length=250),
        ),
    ]
