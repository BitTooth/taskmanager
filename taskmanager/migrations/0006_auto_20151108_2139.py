# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_auto_20151108_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=1024),
        ),
    ]
