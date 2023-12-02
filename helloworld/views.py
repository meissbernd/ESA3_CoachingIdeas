from django.shortcuts import render


# Create your views here.


def get_hello_world(request):
    response = render(
        request, "hello_world.html", {"my_message": "Hello World, Django"}
    )
    return response
