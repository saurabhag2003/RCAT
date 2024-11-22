from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    
class Message(models.Model):
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)