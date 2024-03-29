from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer as DjoserUserSerializer



class UserCreationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id","first_name", "last_name", "username", "email","sex","phone","password"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name", "last_name", "email", "username", "sex", "phone"]

class CurrentUser(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        model = User
        fields = ["first_name", "last_name", "email", "username", "sex", "phone", "password"]
        
