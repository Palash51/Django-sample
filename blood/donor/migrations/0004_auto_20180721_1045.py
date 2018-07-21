# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-21 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0003_auto_20180720_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donorinformation',
            old_name='address',
            new_name='city',
        ),
        migrations.AlterField(
            model_name='donorinformation',
            name='group',
            field=models.IntegerField(choices=[(0, 'Blood Group'), (1, 'O+'), (2, 'O-'), (3, 'A+'), (4, 'A-'), (5, 'B+'), (6, 'B-'), (7, 'AB+'), (8, 'AB-')], default=0),
        ),
        migrations.AlterField(
            model_name='donorinformation',
            name='reason',
            field=models.IntegerField(choices=[(0, 'Reason'), (1, 'Interested'), (2, 'Emergency'), (3, 'Other')], default=0),
        ),
    ]
