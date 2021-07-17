from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Voter(models.Model):
    First_Name=models.CharField(max_length=50,null=False)
    Last_Name=models.CharField(max_length=50)
    Email_Id=models.CharField(max_length=100,primary_key=True)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

