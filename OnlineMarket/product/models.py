from django.db import models
from django.core.validators import MinValueValidator
from user.models import User


class Post(models.Model):
    TYPECHOICE = [
        ("FD","Food"),
        ("PC","Personal Computer"),
        ("MB","Mobile"),
        ("OE", "Other Electronics"),
        ("SK","Sticker"),
        ("CL","Clothes"),
        ("ST", "Stationary"),
        ("BG","Bag"),
        ("OT","Other"),

    ]
    title = models.CharField(max_length = 255)
    description = models.TextField(null = True,blank =True)
    price = models.DecimalField(max_digits = 8, decimal_places = 2, validators = [MinValueValidator(1)])
    type = models.CharField(max_length = 2, choices = TYPECHOICE, default = "OT")
    posted_date = models.DateField(auto_now_add = True)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    review = models.TextField()
    review_date = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.review

