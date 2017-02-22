# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0002_auto_20170221_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='txtfile',
            name='qqfilesolved',
            field=models.FileField(null=True, upload_to='cargo_app/'),
        ),
    ]
