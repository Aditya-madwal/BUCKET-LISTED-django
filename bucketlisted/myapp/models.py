from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class item(models.Model) :
    link = models.CharField(max_length=1000)
    name = models.CharField(max_length=150, blank=True, null=True)
    imgsrc = models.CharField(max_length = 1000,blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    shopper = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
