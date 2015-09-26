# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0011_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
