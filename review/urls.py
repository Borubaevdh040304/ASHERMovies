from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('comments', CommetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rating/', CreateRatingAPIView.as_view()),
    path('favorite/', FavoriteView.as_view()),
    path('add_favorite/<int:m_id>/', add_to_favorite),
    path('toggle_like/<int:m_id>/', toggle_like),
#     path('like-or-dislike/', like_or_dislike),
#     path('user-like/', user_like)
]