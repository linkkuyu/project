# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=1000)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
