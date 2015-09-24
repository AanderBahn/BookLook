# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0006_auto_20150917_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
