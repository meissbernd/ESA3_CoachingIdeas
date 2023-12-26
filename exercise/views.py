from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView

from exercise.models import Exercise


# Create your views here.


def get_exercise_list(request):
    exercises = Exercise.objects.all().order_by("created_on")
    response = render(
        request,
        template_name="exercise/exercise_list.html",
        context={"page_title": "Trainingsübungen", "exercises": exercises},
    )
    return response


class ExerciseHome(ListView):
    model = Exercise
    template_name = "exercise/exercise_home.html"


class ExerciseCreate(CreateView):
    model = Exercise
    template_name = "exercise/exercise_create.html"
    fields = "__all__"
    success_url = reverse_lazy("exercise_start")


class ExerciseDetail(DetailView):
    model = Exercise
    template_name = "exercise/exercise_detail.html"
