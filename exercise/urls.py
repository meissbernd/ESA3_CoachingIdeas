from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from exercise.views import (
    ExerciseCreate,
    ExerciseDetail,
    ExerciseHome,
    ExerciseUpdate,
    ExerciseDelete,
)

from exercise import views

urlpatterns = [
    # path("", ExerciseHome.as_view(), name="exercise_start"),
    path("", views.get_exercise_list, name="exercise_list"),
    path("new/", ExerciseCreate.as_view(), name="exercise_new"),
    path("<int:pk>/", ExerciseDetail.as_view(), name="exercise_detail"),
    path("<int:pk>/update", ExerciseUpdate.as_view(), name="exercise_update"),
    path("<int:pk>/delete", ExerciseDelete.as_view(), name="exercise_delete"),
]

# add a path to core/media (to have access to local stored files)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
