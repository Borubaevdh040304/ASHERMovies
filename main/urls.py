from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, GenreViewSet, MovieViewSet

router = DefaultRouter()
router.register('countries', CountryViewSet)
router.register('genres', GenreViewSet)
router.register('movies', MovieViewSet)

urlpatterns =[
    path('', include(router.urls)),
]

