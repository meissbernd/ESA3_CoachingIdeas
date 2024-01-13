import http

from django.test import TestCase, Client
from django.urls import reverse


class GetExerciseListTest(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)

    def test_home_page_can_be_called(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, http.HTTPStatus.FOUND)
