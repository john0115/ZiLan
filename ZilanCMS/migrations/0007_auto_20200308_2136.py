# Generated by Django 3.0.1 on 2020-03-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZilanCMS', '0006_auto_20200307_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='filetype',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='是否已删除'),
        ),
        migrations.AddField(
            model_name='usertype',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='是否已删除'),
        ),
    ]