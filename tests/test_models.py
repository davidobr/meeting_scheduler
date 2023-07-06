from django.test import TestCase
from meetings.models import Meeting, Room


class MeetingsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Meeting.objects.create(meeting_title='first meeting', meeting_duration='1', date='2023-10-10',
                               start_time='21:00:11', room_id='1')

        Room.objects.create(room_name='Django Room', room_number='18', floor_number='1')
