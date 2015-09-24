# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0002_reviewer_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
