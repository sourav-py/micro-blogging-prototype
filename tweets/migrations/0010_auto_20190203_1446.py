# Generated by Django 2.1.5 on 2019-02-03 09:16

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_auto_20190203_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='author',
            field=models.CharField(max_length=30, verbose_name=django.contrib.auth.models.User),
        ),
    ]
