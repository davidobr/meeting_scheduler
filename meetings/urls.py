from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:meeting_id>', views.meeting_details, name="meeting_details")
]
