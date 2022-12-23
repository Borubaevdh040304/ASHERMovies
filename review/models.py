# from django.conf import settings
# from django.contrib.auth import get_user_model
from django.db import models
from checkaccount.models import User
from main.models import Movie


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}: {self.body}"


class Favourite(models.Model):
    user = models.ForeignKey(User, related_name='favourite', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name='movie_favourite',  on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} -> {self.movie}'


class Rating(models.Model):
    user = models.ForeignKey(User, related_name='rating', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_rating', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)])

    def __str__(self) -> str:
        return f'{self.user} -> {self.movie}'



class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_likes', on_delete=models.CASCADE)

    def str(self):
        return f'{self.user} -> {self.movie}'   