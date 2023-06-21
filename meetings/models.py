from django.db import models


class Meeting(models.Model):
    meeting_title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    meeting_duration = models.IntegerField()

    def __str__(self):
        return f"{self.meeting_title} is at {self.start_time} on {self.date} and lasts for {self.meeting_duration} hour"
