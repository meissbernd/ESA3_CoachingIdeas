from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_hello_world(request):
    response = HttpResponse("Hello World")
    return response
