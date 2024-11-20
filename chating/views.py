from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#room.html을 보여주는 함수
def room(request, room_name):
    return render(request, 'room.html', {'room_name': room_name})

