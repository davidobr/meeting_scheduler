from django.shortcuts import render, get_object_or_404

from meetings.models import Room


def room_details(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, "rooms/room_details.html", {"room": room})


def update_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, "rooms/update_room.html", {"room": room})
