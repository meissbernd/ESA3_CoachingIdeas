import http

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestLandingPage(TestCase):
    def test_home_when_user_is_not_logged_in(self):
        client = Client()
        response = client.get(reverse("home"))
        self.assertEqual(http.HTTPStatus.OK, response.status_code)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "<title>ESA3 CoachingIdeas</title>")
        self.assertContains(response, "Login")
        self.assertContains(response, "Sign Up")


class TestCreateExercisePage(TestCase):
    # Todo: Test fails -  login doesn't work yet
    def test_when_user_is_logged_in(self):
        # Create test user and login
        client = Client()
        user = User.objects.create_user(username="test", password="test")
        client.login(username="test", password="test")

        # Testing
        response = self.client.get(reverse("create_exercise"))
        self.assertEqual(http.HTTPStatus.OK, response.status_code)

        # Logout and delete test user
        client.logout()
        user.delete()
