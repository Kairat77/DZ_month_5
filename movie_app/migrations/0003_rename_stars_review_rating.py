# Generated by Django 4.2.3 on 2023-07-20 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_rating_review_stars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='stars',
            new_name='rating',
        ),
    ]
