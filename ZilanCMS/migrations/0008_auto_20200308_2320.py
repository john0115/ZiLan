# Generated by Django 3.0.1 on 2020-03-08 23:20

import ZilanCMS.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZilanCMS', '0007_auto_20200308_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basearticle',
            name='enclosure',
            field=models.FileField(null=True, upload_to=ZilanCMS.models.user_directory_path, verbose_name='文件存储位置'),
        ),
    ]