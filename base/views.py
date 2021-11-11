from django.shortcuts import render
# We import our models(Room)
from .models import Room

# Create your views here.


# rooms = [
#     {'id':1, 'name': 'Lets learn python!'},
#     {'id':2, 'name': 'Design with me'},
#     {'id':3, 'name': 'Frontend developers'},
# ]




def home(request):
    # Using model manager to get all objects from our model or do diffrent methods like .get(), .filter(), exclude
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


# we pass pk here so we can use our dinamic link
def room(request, pk):
    # here we send only when the object id is = to our primary key (pk)
    room = Room.objects.get( id = pk )
    context = {'room': room}
    return render(request, 'base/room.html', context)