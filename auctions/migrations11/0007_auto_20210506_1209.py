# Generated by Django 3.1.5 on 2021-05-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_comment_listingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='listingid',
            field=models.IntegerField(),
        ),
    ]
