# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(to='taskmanager.Task', null=True),
        ),
    ]
