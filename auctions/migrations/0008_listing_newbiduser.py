# Generated by Django 3.1.5 on 2021-06-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210527_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='newbiduser',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
