from django.db import models

# Create your models here.
class Message(models.Model):
    author = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #room = models.CharField(max_length=300)

    def __str__(self):
        return self.author
    
class Room(models.Model):
    room_name = models.CharField(max_length=200, primary_key=True)
    room_pass = models.CharField(max_length=100)