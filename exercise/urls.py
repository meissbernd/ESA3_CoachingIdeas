from django.urls import path

from exercise.views import (
    create_comment,
    create_exercise,
    delete_comment,
    delete_exercise,
    detail,
    update_comment,
    update_exercise,
)

urlpatterns = [
    path("<int:exercise_id>", detail, name="detail"),
    path("<int:exercise_id>/create_comment", create_comment, name="create_comment"),
    path("comment/<int:comment_id>", update_comment, name="update_comment"),
    path("comment/<int:comment_id>/delete", delete_comment, name="delete_comment"),
    path("create_exercise/", create_exercise, name="create_exercise"),
    path("exercise/<int:exercise_id>", update_exercise, name="update_exercise"),
    path(
        "exercise/<int:exercise_id>/delete/",
        delete_exercise,
        name="delete_exercise",
    ),
]
