# Generated by Django 2.2.5 on 2022-03-26 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0009_auto_20220326_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foundrecor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(max_length=128, upload_to='lost/', verbose_name='照片')),
                ('thing', models.CharField(max_length=32, verbose_name='捡的物品')),
                ('found_time', models.DateField(verbose_name='捡的时间')),
                ('name', models.CharField(max_length=32, verbose_name='拾主姓名')),
                ('link', models.CharField(max_length=11, verbose_name='拾   主联系方式/(QQ/微信)')),
                ('description', models.TextField(max_length=64, verbose_name='描述')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_app.Location', verbose_name='捡的位置')),
                ('sort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_app.Sort', verbose_name='种类')),
            ],
        ),
    ]
