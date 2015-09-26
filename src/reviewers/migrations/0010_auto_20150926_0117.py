# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0009_auto_20150926_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewerbooks',
            name='booked',
        ),
        migrations.RemoveField(
            model_name='reviewerbooks',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reviewerbooks',
            name='nameall',
        ),
        migrations.DeleteModel(
            name='ReviewerBooks',
        ),
    ]
