# Generated by Django 3.1.5 on 2021-05-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210506_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='listingid',
            field=models.IntegerField(null=True),
        ),
    ]
