# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0003_txtfile_qqfilesolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='txtfile',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='txtfile',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='txtfile',
            name='qqtotalweight',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='txtfile',
            name='qquserid',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='txtfile',
            name='qqworkdays',
            field=models.IntegerField(null=True),
        ),
    ]
