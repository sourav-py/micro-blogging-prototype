# Generated by Django 2.1.5 on 2019-02-03 09:23

import django.contrib.auth.base_user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0013_auto_20190203_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='author',
            field=models.CharField(default=django.contrib.auth.base_user.AbstractBaseUser.get_username, max_length=50),
        ),
    ]
