# Generated by Django 2.1.5 on 2019-02-03 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0024_auto_20190203_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='author',
            field=models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
