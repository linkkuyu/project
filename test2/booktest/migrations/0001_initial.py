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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bput_date', models.DateTimeField(db_column=b'pub_date')),
                ('bread', models.IntegerField(default=0)),
                ('bcommet', models.IntegerField()),
                ('isDelet', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'booktest',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('hcontent', models.CharField(max_length=1000)),
                ('isDelet', models.BooleanField(verbose_name=False)),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
