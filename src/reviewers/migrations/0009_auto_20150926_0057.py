# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0008_auto_20150924_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewerBooks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='reviewer',
            name='ref_name',
            field=models.CharField(default=b'ABC', max_length=120),
        ),
        migrations.AddField(
            model_name='reviewerbooks',
            name='booked',
            field=models.ManyToManyField(related_name='booked', null=True, to='reviewers.Reviewer', blank=True),
        ),
        migrations.AddField(
            model_name='reviewerbooks',
            name='name',
            field=models.OneToOneField(related_name='Reviewed', to='reviewers.Reviewer'),
        ),
        migrations.AddField(
            model_name='reviewerbooks',
            name='nameall',
            field=models.ForeignKey(related_name='nameall', to='reviewers.Reviewer'),
        ),
    ]
