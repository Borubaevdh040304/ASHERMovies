# Generated by Django 4.1.4 on 2022-12-20 06:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_dislike',
            field=models.ManyToManyField(blank=True, related_name='post_disliked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_like',
            field=models.ManyToManyField(blank=True, related_name='post_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('FANTASY', 'Fantasy'), ('HORROR', 'Horror'), ('THRILLER', 'Thriller')], max_length=100),
        ),
    ]