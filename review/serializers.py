from rest_framework.serializers import ModelSerializer
from .models import Comment, Rating, Favourite, Like


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # exclude = ('user',)
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
