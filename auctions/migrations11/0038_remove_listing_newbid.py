# Generated by Django 3.1.5 on 2021-05-27 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0037_auto_20210525_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='newbid',
        ),
    ]
