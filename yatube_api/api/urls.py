from rest_framework.routers import DefaultRouter
from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowList


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/follow/', FollowList.as_view(), name='follow-list'),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
