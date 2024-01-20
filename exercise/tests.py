import http

# from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

# Get user model from settings
from django.contrib.auth import get_user_model

User = get_user_model()


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
    """Tests for creating an exercise page."""

    def setUp(self):
        # Create test user
        self.test_user = User.objects.create_user(
            username="testuser", password="testuser"
        )
        self.test_user.save()

    def test_redirect_when_not_logged_in(self):
        """Test user is redirected to login page."""
        # Testing
        response = self.client.get(reverse("create_exercise"))
        # Assertion
        self.assertRedirects(
            response, "/accounts/login/?next=/exercise/create_exercise/"
        )

    def test_when_logged_in(self):
        """Test logged-in user can see page."""
        # Login test user
        login = self.client.login(username="testuser", password="testuser")
        # Testing
        response = self.client.get(reverse("create_exercise"))
        # Assertions
        self.assertEqual(str(response.context["user"]), "testuser")
        self.assertEqual(http.HTTPStatus.OK, response.status_code)
