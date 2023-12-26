from django.urls import path
from exercise.views import ExerciseCreate, ExerciseHome

urlpatterns = [
    path("", ExerciseHome.as_view(), name="exercise_start"),
    path("new/", ExerciseCreate.as_view(), name="exercise_new"),
]
