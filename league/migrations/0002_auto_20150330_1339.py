# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('name', 'mascot'), 'verbose_name_plural': 'Teams'},
        ),
        migrations.RemoveField(
            model_name='team',
            name='callnumber',
        ),
        migrations.RemoveField(
            model_name='team',
            name='date',
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='mascot',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
