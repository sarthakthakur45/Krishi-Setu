# Generated by Django 3.0.8 on 2021-04-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210416_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='ratings',
            field=models.IntegerField(),
        ),
    ]
