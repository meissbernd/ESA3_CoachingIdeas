from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise


# Create your views here.
def home(request):
    search_exercise = request.GET.get("searchExercise")
    if search_exercise:
        exercises = Exercise.objects.filter(title__icontains=search_exercise)
    else:
        exercises = Exercise.objects.all()

    return render(request, "home.html",
                  {"searchExercise": search_exercise,
                   "exercises": exercises})


def exercise_list(request):
    exercises = Exercise.objects.all().order_by("created_on")
    return render(request,
                  "exercise_list.html",
                  {"page_title": "Trainingsübungen",
                   "exercises": exercises})


def about(request):
    return HttpResponse("<h1>About")
