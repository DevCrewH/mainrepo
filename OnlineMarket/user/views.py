from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer, UserCreationSerializer
from .models import User

class UserViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["first_name", "last_name", "username"]
    
    def get_queryset(self):
        if self.request.method == "PUT":
            return User.objects.filter(id = self.request.user.id)
        elif self.request.method == "PATCH":
            return User.objects.filter(id = self.request.user.id)
        elif self.request.method == "DELETE":
            return User.objects.filter(id = self.request.user.id)
        else:
            return User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        return UserCreationSerializer







