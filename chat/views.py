from django.shortcuts import render, get_object_or_404
from django.views import View

from chat.models import Room, Message


class HomeView(View):
    def get(self, request):
        return render(request, "chat/home.html")


class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, "chat/rooms.html", {"rooms": rooms})


class RoomView(View):
    def get(self, request, slug):
        room = get_object_or_404(Room, slug=slug)
        messages = Message.objects.filter(room=room)
        return render(request, "chat/room.html", {"room": room, "messages": messages})
