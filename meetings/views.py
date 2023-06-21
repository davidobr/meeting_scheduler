from django.shortcuts import render, get_object_or_404
from .models import Meeting


def meeting_details(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, "meetings/meeting_details.html", {"meeting": meeting})
