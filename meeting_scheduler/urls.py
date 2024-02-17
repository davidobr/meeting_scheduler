"""
URL configuration for meeting_scheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website.views import homepage, meeting, rooms, UpdateMeeting, CreateMeeting, DeleteMeeting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="home"),
    path('meetings', meeting, name="meetings"),
    path('meetings/details/', include('meetings.urls'), name="meeting_details"),
    path('meetings/create', CreateMeeting.as_view(), name="create_meeting"),
    path('meetings/update/<pk>', UpdateMeeting.as_view(), name="update_meeting"),
    path('meetings/delete/<pk>', DeleteMeeting.as_view(), name="delete_meeting"),
    path('rooms', rooms, name="rooms"),
    path('rooms/', include('rooms.urls')),
]
