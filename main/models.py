from django.db import models
from django.db.models import Q
from checkaccount.models import User

# GENRE = [
#     ('ACTION', 'Action'),
#     ('ADVENTURE', 'Adventure'),
#     ('COMEDY', 'Comedy'),
#     ('DRAMA', 'drama'),
#     ('FANTASY', 'Fantasy'),
#     ('HORROR', 'Horror'),
#     ('MUSICALS', 'Musicals'),
#     ('MYSTERY', 'Mystery'),
#     ('ROMANCE', 'Romance'),
#     ('THRILLER', 'Thriller'),
#     ('WESTERN', 'Western')
# ]


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Movie.objects.filter(draft=False).values("created_year")

    

class Genre(models.Model):
    title = models.CharField(max_length=25)

    def ____str____(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    
class Country(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Movie(GenreYear,models.Model):
    genre = models.ManyToManyField(Genre, blank=True)
    country = models.ForeignKey(Country, related_name='country_movie', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.IntegerField(default=0, help_text="указывать сумму в долларах")
    created_year = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media', null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
    
    @property
    def average_rating(self):
        ratings = self.movie_rating.all() # это queryset  со значениями ratings
        values = []
        for rating in ratings:
            values.append(rating.value)
        if values:
            return sum(values) / len(values)
        return 0



# class FilterMoviesView(GenreYear):
#     def get_queryset(self):
#         year = Movie.created_year
#         queryset = Movie.objects.filter(
#         Q(year__in=self.get_years("created_year")) |
#         Q(genres__in=self.get_genres("genre"))
#         )
#         return queryset 