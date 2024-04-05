from rest_framework import serializers
from django.db.models.aggregates import Avg
from .models import User
from product.models import Product, Rating
from djoser.serializers import UserCreateSerializer, UserSerializer as DjoserUserSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "rating", "price", "image"]
    
    rating = serializers.SerializerMethodField(method_name= "rating_calculate")
    
    def rating_calculate(self,product:Product):
        average = Rating.objects.filter(product_id = product.id).aggregate(average=Avg("rate"))
        return average["average"]
    

class UserCreationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id","first_name", "last_name", "username", "email","sex","phone","password"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name", "last_name", "email", "username", "sex", "phone", "product"]
    
    product = ProductSerializer(many=True)

class CurrentUser(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        model = User
        fields = ["first_name", "last_name", "email", "username", "sex", "phone", "password"]
        
