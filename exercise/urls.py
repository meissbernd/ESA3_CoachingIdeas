from django.urls import path
from . import views
from .views import create_exercise

urlpatterns = [
    path('<int:exercise_id>', views.detail, name='detail'),
    path('<int:exercise_id>/create_comment', views.create_comment, name='create_comment'),
    path('comment/<int:comment_id>', views.update_comment, name='update_comment'),
    path('comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('create_exercise/', views.create_exercise, name='create_exercise'),
    path('exercise/<int:exercise_id>', views.update_exercise, name='update_exercise'),
    path('exercise/<int:exercise_id>/delete/', views.delete_exercise, name='delete_exercise'),
]
