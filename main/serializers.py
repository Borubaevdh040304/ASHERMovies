from rest_framework.serializers import ModelSerializer
from .models import *
from review.models import Comment

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
    

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance:Movie):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.movie_comments.all(), many=True).data
        rep['rating'] = instance.average_rating
        rep['likes'] = instance.movie_likes.all().count()
        rep['favorites'] = instance.movie_favourite.filter(favorite=True).count()
        return rep

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['user']
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.email
        rep['movie'] = instance.movie.title
        return rep