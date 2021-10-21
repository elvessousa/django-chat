from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    user = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
