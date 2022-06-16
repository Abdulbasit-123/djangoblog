from django.db import models
from django.contrib.auth import get_user_model

class Post(models.model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey (get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateField()
    Published_date = models.DateTimeField()

def __str__(self):
    return self.title