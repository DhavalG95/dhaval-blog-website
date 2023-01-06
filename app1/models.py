from django.db import models
from django.conf import settings


# Create your models here.
class Form(models.Model):
    Title = models.CharField(max_length=500)
    Description = models.CharField(max_length=50000)
    Author = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    # user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Title

class Contactform(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.IntegerField()
    Email = models.EmailField(max_length=100)
    Query = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Comment(models.Model):
    Name = models.CharField(max_length=256)
    Content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    Post = models.ForeignKey(Form,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return self.Name