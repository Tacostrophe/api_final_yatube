from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, 'posts')
router.register(r'groups', views.GroupViewSet, 'groups')
router.register(r'follow', views.FollowViewSet, 'follow')
router.register(r'posts/(?P<post_id>\d+)/comments',
                views.CommentsViewSet, 'comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
