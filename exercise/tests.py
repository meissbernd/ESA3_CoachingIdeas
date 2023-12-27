from django.test import RequestFactory, TestCase
from django.http import HttpRequest
from exercise.views import ExerciseHome


class ExerciseHomeViewTest(TestCase):
    def test_html_contains_correct_title(self):
        request = RequestFactory().get("/")
        view = ExerciseHome()
        view.setup(request)
        response = ExerciseHome.as_view()(request)
        html = response.rendered_content
        self.assertIn("<title>Trainingsübungen</title>", html)
