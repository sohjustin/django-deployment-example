from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    first_Name = models.CharField(max_length = 150)
    last_Name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 250)

    def __str__(self):
        return self.first_Name

class SignIn(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

    def __str(self):
        return self.name

class UsesrProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank = True)
    portfolio_pic = models.ImageField(upload_to = "profile_pics", blank = True)

    def __str__(self):
        return self.user.username
