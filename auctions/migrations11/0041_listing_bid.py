# Generated by Django 3.1.5 on 2021-05-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_bid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
