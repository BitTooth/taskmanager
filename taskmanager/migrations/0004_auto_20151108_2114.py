# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20151108_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_date',
            field=models.DateTimeField(verbose_name=b'done date', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name=b'due date', blank=True),
        ),
    ]
