# Generated by Django 5.0.1 on 2024-01-07 01:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('latest_movie', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('premiere_date', models.DateField()),
                ('category', models.CharField(default=' ', max_length=200)),
                (
                    'academy_awards',
                    models.SmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(11),
                        ]
                    ),
                ),
                (
                    'director_id',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='movies',
                        to='core.directors',
                    ),
                ),
                (
                    'lead_actor_id',
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='core.actors'
                    ),
                ),
            ],
        ),
    ]
