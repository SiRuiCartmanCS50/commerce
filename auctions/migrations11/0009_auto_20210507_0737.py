# Generated by Django 3.1.5 on 2021-05-07 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210506_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.CharField(max_length=33),
        ),
    ]
