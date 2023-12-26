from django.urls import path
from exercise.views import ExerciseHome

urlpatterns = [
    path("", ExerciseHome.as_view(), name="exercise_start"),
]
