from django.shortcuts import render

# Create your views here.


rooms = [
    {'id':1, 'name': 'Lets learn python!'},
    {'id':2, 'name': 'Design with me'},
    {'id':3, 'name': 'Frontend developers'},
]




def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


# we pass pk here so we can use our dinamic link
def room(request, pk):
    # with a forloop we can acces each room if our id is = our pk in our link 
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)