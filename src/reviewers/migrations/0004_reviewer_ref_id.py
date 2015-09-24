# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0003_auto_20150916_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='ref_id',
            field=models.CharField(default=b'ABC', max_length=120),
        ),
    ]
