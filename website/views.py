from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, DeleteView

from meetings.models import Meeting, Room


def homepage(request):
    all_meetings = Meeting.objects.count()
    return render(request, 'website/homepage.html', {'all_meetings': all_meetings})


def meeting(request):
    current_meetings = Meeting.objects.all()
    meetings_count = Meeting.objects.count()
    return render(request, 'website/meetings.html', {'meetings': current_meetings, 'meeting_count': meetings_count})


class CreateMeeting(CreateView):
    model = Meeting
    template_name = "website/create_meeting.html"
    fields = ["meeting_title", "date", "start_time", "meeting_duration", "room"]
    success_url = "/meetings"


class UpdateMeeting(UpdateView):
    model = Meeting
    template_name = "website/meeting_update.html"
    fields = ["meeting_title", "date", "start_time", "meeting_duration", "room"]
    success_url = "/meetings"


class DeleteMeeting(DeleteView):
    model = Meeting
    template_name = "website/delete_meeting.html"
    success_url = "/meetings"


def rooms(request):
    rooms_page = Room.objects.all()
    return render(request, 'website/rooms.html', {'rooms': rooms_page})
