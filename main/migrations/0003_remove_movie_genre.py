# Generated by Django 4.1.4 on 2022-12-20 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_movie_dislike_movie_movie_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
    ]
