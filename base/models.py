from django.db import models
from django.db.models.base import Model
# Here we add user model from django
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



# we create our first model for our server with a SQL server
class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    # Here auto_now will changed every times we update 
    updated = models.DateTimeField(auto_now=True)
    # Here auto_now_add will add once we create and will never change again
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Here we add room to connect to its parents id that is Room with this method models.foreignKey, and with on_delete = models.CASCADE we delete the children messages if the parent(Room) got deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # Again we send text inside the body as a string with this method and we only show first 50 characters
    def __str__(self):
        return self.body[ 0:50 ]