# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0005_remove_reviewer_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
