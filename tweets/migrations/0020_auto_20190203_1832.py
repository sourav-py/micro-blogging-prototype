# Generated by Django 2.1.5 on 2019-02-03 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0019_auto_20190203_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
