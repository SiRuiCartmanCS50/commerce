# Generated by Django 3.1.5 on 2021-05-27 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210527_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='newbid',
        ),
    ]
