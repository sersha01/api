from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    def __str__(self):
        s = self.username 
        return s + ' ' + str(self.id)

class Book(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True, default='')
    description = models.TextField()
    telete = models.BooleanField(default=False)