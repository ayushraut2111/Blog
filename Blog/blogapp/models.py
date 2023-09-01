from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    Author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Title=models.TextField()
    Body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

