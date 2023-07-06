from django.test import TestCase


class ViewsAreVisibleTest(TestCase):

    def test_can_render_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_can_render_meetings(self):
        response = self.client.get('/meetings')
        self.assertEqual(response.status_code, 200)

    # This test will fail until I've worked out how to test the model, store data in the database and then test this
    # view
    # def test_can_render_meeting_details(self):
    #     response = self.client.get('/meetings/1')
    #     self.assertEqual(response.status_code, 200)

    def test_can_render_rooms(self):
        response = self.client.get('/rooms')
        self.assertEqual(response.status_code, 200)
