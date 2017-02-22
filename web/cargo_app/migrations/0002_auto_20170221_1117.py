# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='txtfile',
            name='qqchunksize',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='txtfile',
            name='qqfilename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='txtfile',
            name='qqpartbyteoffset',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='txtfile',
            name='qqpartindex',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='txtfile',
            name='qqtotalfilesize',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='txtfile',
            name='qqtotalparts',
            field=models.IntegerField(null=True),
        ),
    ]
