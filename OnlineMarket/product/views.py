from django.shortcuts import render
from .serializers import PostSerializer, ReviewSerializer, CreateReviewSerializer
from .models import Post, Review
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateReviewSerializer
        return ReviewSerializer

    def get_serializer_context(self):
        return {
            "post_id" : self.kwargs["post_pk"],
            "user_id" : self.request.user.id
            }


