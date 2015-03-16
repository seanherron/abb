# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
                ('records', models.ManyToManyField(to='hours.Record')),
                ('reporting_period', models.ForeignKey(to='hours.ReportingPeriod')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='record',
            name='created',
        ),
        migrations.RemoveField(
            model_name='record',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='record',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='record',
            name='reporting_period',
        ),
    ]
