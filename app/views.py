from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import routers, serializers, viewsets

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = member.objects.all()
    serializer_class = MemberSerializer