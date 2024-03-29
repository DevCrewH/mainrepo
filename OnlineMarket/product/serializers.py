from rest_framework import serializers
from .models import Post, Review
from user.models import User

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "price", "type", "posted_date", "image"]
    
    def create(self, validated_data):
        user = User.objects.get(id = self.context["user_id"])
        return Post.objects.create(user = user, **validated_data)

class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","user","title", "description", "price", "type", "posted_date","image"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id","user","review", "review_date"]

class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "review"]
    def create(self, validated_data):
        post_id = self.context["post_id"]
        user = User.objects.get(id = self.context["user_id"])
        return Review.objects.create(post_id= post_id, user = user ,**validated_data)
    
