from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=100,default="")
    Director=models.CharField(max_length=100,default="")
    Date=models.DateField(default=datetime.now, blank=True)
    Upvote=models.IntegerField(default=0)
    Main_character=models.TextField(max_length=100, default="")
    Age=models.CharField(max_length=100,default="")
    Birthplace=models.TextField(max_length=200,default="")
    image=models.URLField(max_length=10000, default=None,null=True)



def __str__(self):
    return str(self.name)
