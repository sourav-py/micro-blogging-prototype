# Generated by Django 2.1.5 on 2019-02-03 13:05

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0020_auto_20190203_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='author',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=30),
        ),
    ]
