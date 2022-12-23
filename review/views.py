from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .serializers import CommentSerializer, FavouriteSerializer,  RatingSerializer
from .models import Comment, Rating, Favourite, Like 

from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from checkaccount.models import User
from main.models import Movie

class CommetViewSet(ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer


class CreateRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        user = request.user
        serializer = RatingSerializer(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        movie_id = request.data.get("movie")
        if Rating.objects.filter(user=user, movie__id=movie_id).exists():
            rating = Rating.objects.get(user=user, movie__id=movie_id)
            rating.value = request.data.get("value")
            rating.save()
        else:
            serializer.save()
        return Response(status=201)
        

@api_view(['POST'])
def add_to_favorite(request, m_id):
    user = request.user
    movie = get_object_or_404(Movie, id=m_id)

    if Favourite.objects.filter(user=user, movie=movie).exists():
        Favourite.objects.filter(user=user, movie=movie).delete()
        return Response('Deleted from favorite')
    else:
        Favourite.objects.create(user=user, movie=movie, favorite=True)
        return Response('Added to favorites')

class FavoriteView(ListAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthenticated, ]

    def filter_queryset(self, queryset):
        new_queryset = queryset.filter(user=self.request.user)
        return new_queryset

@api_view(['GET'])
def toggle_like(request, m_id):
    user = request.user
    movie = get_object_or_404(Movie, id=m_id)

    if Like.objects.filter(user=user, movie=movie).exists():
        Like.objects.filter(user=user, movie=movie).delete()
        return Response ('Like has been deleted')
    else:
        Like.objects.create(user=user, movie=movie)
        return Response("Like toggled", 200)