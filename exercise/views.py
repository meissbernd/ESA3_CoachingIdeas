from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    search_exercise = request.GET.get("searchExercise")
    return render(request, "home.html",
                  {"searchExercise": search_exercise})


def about(request):
    return HttpResponse("<h1>About")
