from django.shortcuts import render

from meetings.models import Meeting, Room


def homepage(request):
    all_meetings = Meeting.objects.count()
    return render(request, 'website/homepage.html', {'all_meetings': all_meetings})


def meeting(request):
    current_meetings = Meeting.objects.all()
    meetings_count = Meeting.objects.count()
    return render(request, 'website/meetings.html', {'meetings': current_meetings, 'meeting_count': meetings_count})


def rooms(request):
    rooms_page = Room.objects.all()
    return render(request, 'website/rooms.html', {'rooms': rooms_page})
