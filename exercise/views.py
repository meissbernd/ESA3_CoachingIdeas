from django.shortcuts import render

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
