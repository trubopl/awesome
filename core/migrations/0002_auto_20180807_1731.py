# Generated by Django 2.0.7 on 2018-08-07 17:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 7, 17, 31, 35, 54646, tzinfo=utc), null=True),
        ),
    ]
