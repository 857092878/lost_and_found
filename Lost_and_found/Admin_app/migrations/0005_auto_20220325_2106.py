# Generated by Django 2.2.5 on 2022-03-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0004_lost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='link',
            field=models.IntegerField(max_length=11, verbose_name='失主练习方式/(QQ/微信)'),
        ),
    ]