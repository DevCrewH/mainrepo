from rest_framework import serializers
from django.db.models.aggregates import Avg
from .models import Post, Review, Rating
from user.models import User


class GetRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate"]

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
        fields = ["id","user","title", "description", "price", "type", "posted_date","image","rating"]
    
    rating = serializers.SerializerMethodField(method_name= "rating_calculate")
    
    def rating_calculate(self,post:Post):
        average = Rating.objects.filter(post_id = post.id).aggregate(average=Avg("rate"))
        return average["average"]

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
    
class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate"]
    
    def create(self, validated_data):
        post_id = self.context["post_id"]
        user_id = self.context["user_id"]

        return Rating.objects.create(post_id=post_id, user_id=user_id,**validated_data)
