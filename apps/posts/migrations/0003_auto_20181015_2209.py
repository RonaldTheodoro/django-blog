# Generated by Django 2.1.2 on 2018-10-16 01:09

import contrib.utils
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181014_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=contrib.utils.upload_file_path, verbose_name='image'),
        ),
    ]
