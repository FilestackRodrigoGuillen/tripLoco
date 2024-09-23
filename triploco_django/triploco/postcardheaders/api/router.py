from django.urls import path
from rest_framework.routers import DefaultRouter

from postcardheaders.api.views import PostCardHeaderApiViewSet

router_postheaders = DefaultRouter()

router_postheaders.register(
    prefix = "postheaders", basename = "postheaders", viewset = PostCardHeaderApiViewSet
)