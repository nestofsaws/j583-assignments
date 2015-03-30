# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('playerid', models.CharField(unique=True, max_length=12)),
                ('number', models.IntegerField(max_length=3, null=True)),
            ],
            options={
                'ordering': ('number', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('callnumber', models.CharField(max_length=4, null=True)),
                ('coach', models.CharField(max_length=50)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('players', models.ManyToManyField(to='league.Player')),
            ],
            options={
                'ordering': ('-date', 'name'),
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
    ]
