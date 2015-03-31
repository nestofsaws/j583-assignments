# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20150330_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='games_played',
            field=models.IntegerField(max_length=3, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='goals',
            field=models.IntegerField(max_length=3, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.IntegerField(max_length=3, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.IntegerField(max_length=3, null=True),
            preserve_default=True,
        ),
    ]
