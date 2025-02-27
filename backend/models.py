from django.db import models

# Create your models here.
class Message(models.Model):
    author = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author