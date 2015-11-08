# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1024)),
                ('create_date', models.DateTimeField(verbose_name=b'creation date')),
                ('due_date', models.DateTimeField(verbose_name=b'due date')),
                ('done_date', models.DateTimeField(verbose_name=b'done date')),
                ('done', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(to='taskmanager.Task')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='taskmanager.Task'),
        ),
    ]
