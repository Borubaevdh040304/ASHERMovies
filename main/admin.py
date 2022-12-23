from django.contrib import admin
from .models import Country, Movie, Genre
from review.models import Comment, Favourite, Rating



class RatingInline(admin.TabularInline):
    model = Rating

class CommentInline(admin.TabularInline):
    model = Comment

class FavouriteInline(admin.TabularInline):
    model = Favourite

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_year' ]
    list_filter = ['created_year']
    search_fields = ['title','created_year']
    

admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Movie, MovieAdmin)

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"
