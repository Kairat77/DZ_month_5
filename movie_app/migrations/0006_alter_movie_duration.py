# Generated by Django 4.2.3 on 2023-08-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_remove_director_movies_count_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]