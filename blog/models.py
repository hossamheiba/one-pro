from django.db import models

# Create your models here.
class Blog(models.Model):
    tim=models.CharField(("tim"), max_length=50),
    tirm=models.CharField(("tirm"), max_length=50),
    
    
