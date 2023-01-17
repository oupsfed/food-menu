from django.urls import include, path
from rest_framework import routers

from .views import RecipeViewSet

router = routers.SimpleRouter()
router.register('recipe', RecipeViewSet)
# router.register(r'recipe/(?P<reci_id>\d+)/comments',
#                 CommentViewSet,
#                 basename='comments')
# router.register('groups', GroupViewSet)
# router.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
