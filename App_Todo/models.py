from django.db import models

# Create your models here.
class tweets(models.Model):
   tweet = models.CharField(max_length=200)
   time = models.DateTimeField(auto_now=True)
   name = models.CharField(max_length=100)