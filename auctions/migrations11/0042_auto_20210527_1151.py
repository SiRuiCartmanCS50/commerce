# Generated by Django 3.1.5 on 2021-05-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0041_listing_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bid',
        ),
        migrations.AddField(
            model_name='listing',
            name='newbid',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
