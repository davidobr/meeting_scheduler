from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:room_id>', views.room_details, name="room_details")
]
