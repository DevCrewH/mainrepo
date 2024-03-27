from rest_framework import serializers
from .models import Post, Review

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "price", "type", "posted_date", "image"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id","user","review", "review_date"]
    
    def create(self, validated_data):
        post_id = self.context["post_id"]
        return Review.objects.create(post_id= post_id, **validated_data)
