from django.shortcuts import render
from .serializers import PostSerializer, ReviewSerializer
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
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {"post_id" : self.kwargs["post_pk"]}



