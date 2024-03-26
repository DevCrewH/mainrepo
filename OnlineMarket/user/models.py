from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SEXCHOICE = [
        ("M" ,"Male"),
        ("F" ,"Female"),
        ("N" ,"Neutral"),
    ]
    email = models.EmailField(unique = True)
    phone = models.IntegerField()
    sex = models.CharField(max_length = 1, choices = SEXCHOICE, default = "N" )


