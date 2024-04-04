from django.shortcuts import render
from .serializers import CreatePostSerializer, GetPostSerializer, ReviewSerializer, CreateReviewSerializer, CreateRatingSerializer, GetRatingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Review, Rating
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter
from django.db import IntegrityError
from rest_framework.response import Response
from django.http import JsonResponse

class ProductViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ["title", "description"]
    ordering_fields = ["posted_time", "rating"]

    def get_queryset(self):
        if self.request.method == "PUT":
            return Product.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Product.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Product.objects.filter(user_id = self.request.user.id)
        else:
            return Product.objects.all()
        
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetPostSerializer
        return CreatePostSerializer
        
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
    

class ReviewViewSet(ModelViewSet):

    def get_queryset(self):
        if self.request.method == "PUT":
            return Review.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Review.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Review.objects.filter(user_id = self.request.user.id)
        else:
            return Review.objects.filter(product_id = self.kwargs["product_pk"])
        
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewSerializer
        return CreateReviewSerializer

    def get_serializer_context(self):
        return {
            "product_id" : self.kwargs["product_pk"],
            "user_id" : self.request.user.id
            }

class RatingViewSet(ModelViewSet):
    try:
        def get_serializer_class(self):
            if self.request.method == "GET":
                return GetRatingSerializer
            return CreateRatingSerializer
        def get_queryset(self):
            if self.request.method == "PUT":
                return Rating.objects.filter(user_id = self.request.user.id)
            elif self.request.method == "PATCH":
                return Rating.objects.filter(user_id = self.request.user.id)
            elif self.request.method == "DELETE":
                return Rating.objects.filter(user_id = self.request.user.id)
            else:
                return Rating.objects.filter(product_id = self.kwargs["product_pk"])
        def get_permissions(self):
            if self.request.method == "GET":
                return [AllowAny()]
            return [IsAuthenticated()]
        def get_serializer_context(self):
            return {
                "product_id" : self.kwargs["product_pk"],
                "user_id" : self.request.user.id
                }
    except IntegrityError:
        def error(request):
            return Response({'error': "You can't rate twice"}, status=400)
    


