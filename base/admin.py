from django.contrib import admin

# Register your models here.
# Here we add our models (Room)
from . models import Room, Topic, Message

# here we wanna add our model and work with it 
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)