from django.test import TestCase

from tests.test_models import MeetingsModelTest, Meeting


class ViewsAreVisibleTest(TestCase):

    def test_can_render_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_can_render_meetings(self):
        response = self.client.get('/meetings')
        self.assertEqual(response.status_code, 200)

    def test_can_render_meeting_details(self):
        MeetingsModelTest.setUpTestData()
        response = self.client.get('/meetings/1')  # I would like to improve this test to take the ID in the response
        # for a truer test, however, knowing I have just entered 1 meeting means I know the ID is 1 and should
        # pass as a test
        self.assertEqual(response.status_code, 200)

    def test_can_render_rooms(self):
        response = self.client.get('/rooms')
        self.assertEqual(response.status_code, 200)
