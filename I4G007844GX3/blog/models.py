from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    Created_date = models.DateTimeField(default=datetime.today)
    Published_date = models.DateTimeField(default=datetime.today)
