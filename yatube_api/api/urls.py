from django.urls import path, include
from rest_framework import routers

from . import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', views.PostViewSet, 'posts')
router_v1.register(r'groups', views.GroupViewSet, 'groups')
router_v1.register(r'follow', views.FollowViewSet, 'follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                views.CommentsViewSet, 'comments')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
