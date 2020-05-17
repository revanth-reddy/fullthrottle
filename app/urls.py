from django.urls import path
from .views import *
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]