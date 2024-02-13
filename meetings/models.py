from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    floor_number = models.IntegerField()

    def __str__(self):
        return f"{self.room_name} (Room number {self.room_number}) is on floor {self.floor_number}"


class Meeting(models.Model):
    meeting_title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    meeting_duration = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.meeting_title} is at {self.start_time} on {self.date} and lasts for {self.meeting_duration} hour"
