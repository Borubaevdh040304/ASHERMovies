from django.contrib import admin
from .models import Rating, Comment, Favourite, Like

class RatingInline(admin.TabularInline):
    model = Rating

class CommentInline(admin.TabularInline):
    model = Comment

class FavouriteInline(admin.TabularInline):
    model = Favourite

class LikeInline(admin.TabularInline):
    model = Like

