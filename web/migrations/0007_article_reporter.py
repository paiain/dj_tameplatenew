# Generated by Django 3.2.6 on 2021-08-27 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0006_auto_20210827_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_line', models.CharField(max_length=255)),
                ('pub_date', models.DateField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.reporter')),
            ],
        ),
    ]