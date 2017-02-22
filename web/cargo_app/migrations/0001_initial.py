# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TxtFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('qqfile', models.FileField(upload_to='cargo_app/')),
                ('qquuid', models.CharField(max_length=255)),
                ('qqfilename', models.CharField(max_length=255)),
                ('qqpartindex', models.IntegerField()),
                ('qqchunksize', models.IntegerField()),
                ('qqpartbyteoffset', models.IntegerField()),
                ('qqtotalfilesize', models.IntegerField()),
                ('qqtotalparts', models.IntegerField()),
            ],
        ),
    ]
