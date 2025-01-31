from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, primary_key=True)    
    bio = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_images/')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username
    

class Post(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='posts')
    description = models.CharField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(MyUser,related_name='post_likes',blank=True)


