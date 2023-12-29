from django.test import RequestFactory, TestCase
from django.http import HttpRequest
from exercise.views import ExerciseHome, get_exercise_list


class GetExerciseListTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = get_exercise_list(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>Trainingsübungen</title>", html)
