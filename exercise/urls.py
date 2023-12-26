from django.urls import path
from exercise.views import ExerciseCreate, ExerciseDetail, ExerciseHome


urlpatterns = [
    path("", ExerciseHome.as_view(), name="exercise_start"),
    path("new/", ExerciseCreate.as_view(), name="exercise_new"),
    path("<int:pk>/", ExerciseDetail.as_view(), name="exercise_detail"),
]