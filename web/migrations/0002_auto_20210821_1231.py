# Generated by Django 3.2.6 on 2021-08-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
