from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Home(TemplateView):
    template_name = "core/home.html"


def upload(request):
    # context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        print(uploaded_file.name)
        print(uploaded_file.size)
    #     fs = FileSystemStorage()
    #     name = fs.save(uploaded_file.name, uploaded_file)
    #     context["url"] = fs.url(name)
    return render(request, "core/upload.html")  # , context)
