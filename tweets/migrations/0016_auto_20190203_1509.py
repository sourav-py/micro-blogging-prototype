# Generated by Django 2.1.5 on 2019-02-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0015_auto_20190203_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='author',
            field=models.CharField(default='auth.User', max_length=30),
        ),
    ]
