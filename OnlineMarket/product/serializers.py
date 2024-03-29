from rest_framework import serializers
from .models import Post, Review
from user.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "price", "type", "posted_date", "image"]
    
    def create(self, validated_data):
        return Post.objects.create(user_id = self.context["user_id"], **validated_data)

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
        return Review.objects.create(post_id= post_id, user_id = self.context["user_id"],**validated_data)
    
