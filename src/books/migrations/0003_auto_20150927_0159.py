# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0012_delete_book'),
        ('books', '0002_auto_20150926_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.TextField(max_length=500)),
                ('reviewer', models.ForeignKey(to='reviewers.Reviewer', unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.ForeignKey(to='books.Book'),
        ),
    ]
