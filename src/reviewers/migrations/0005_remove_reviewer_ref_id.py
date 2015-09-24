# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0004_reviewer_ref_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewer',
            name='ref_id',
        ),
    ]
