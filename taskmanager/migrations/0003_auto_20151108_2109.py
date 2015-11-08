# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20151108_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(blank=True, to='taskmanager.Task', null=True),
        ),
    ]
