from django.urls import path
from exercise.views import (
    ExerciseCreate,
    ExerciseDetail,
    ExerciseHome,
    ExerciseUpdate,
    ExerciseDelete,
)


urlpatterns = [
    path("", ExerciseHome.as_view(), name="exercise_start"),
    path("new/", ExerciseCreate.as_view(), name="exercise_new"),
    path("<int:pk>/", ExerciseDetail.as_view(), name="exercise_detail"),
    path("<int:pk>/update", ExerciseUpdate.as_view(), name="exercise_update"),
    path("<int:pk>/delete", ExerciseDelete.as_view(), name="exercise_delete"),
]
