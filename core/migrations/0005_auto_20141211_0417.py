# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_list_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
