# Generated by Django 2.0.7 on 2018-07-25 19:56

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompaniesCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_amount', models.IntegerField()),
                ('max_amount', models.IntegerField()),
                ('min_days', models.IntegerField()),
                ('max_days', models.IntegerField()),
                ('miscs', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CompaniesLoans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_amount', models.IntegerField()),
                ('max_amount', models.IntegerField()),
                ('min_days', models.IntegerField()),
                ('max_days', models.IntegerField()),
                ('first_free', models.BooleanField()),
                ('amount_first_free', models.IntegerField()),
                ('installment_loan', models.BooleanField()),
                ('installment_min_amount', models.IntegerField()),
                ('installment_max_amount', models.IntegerField()),
                ('installment_min_days', models.IntegerField()),
                ('installment_max_days', models.IntegerField()),
                ('miscs', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 7, 25, 19, 56, 9, 613567, tzinfo=utc), null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('body', models.TextField()),
                ('meta_title', models.CharField(max_length=158)),
                ('meta_description', models.CharField(max_length=320)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
