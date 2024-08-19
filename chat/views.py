from django.shortcuts import render, redirect
from .models import MovieRoom

def create_room(request):
    if request.method == "POST":
        room_name = request.POST['room_name']
        room = MovieRoom.objects.create(name=room_name, host=request.user)
        return redirect('room', room_code=room.code)
    return render(request, 'chat/create_room.html')

def join_room(request):
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        return redirect('room', room_code=room_code)
    return render(request, 'chat/join_room.html')

def room(request, room_code):
    room = MovieRoom.objects.get(code=room_code)
    return render(request, 'chat/room.html', {'room': room})
