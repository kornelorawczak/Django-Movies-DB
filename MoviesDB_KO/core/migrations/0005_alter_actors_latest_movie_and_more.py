# Generated by Django 5.0.1 on 2024-01-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_actors_latest_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='latest_movie',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='directors',
            name='latest_movie',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
    ]
