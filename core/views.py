from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


# Create your views here.


class Home(TemplateView):
    template_name = "core/home.html"


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        # url = fs.url(name)
        # print(url)
        # Put url of uploaded file into context, send to template and use there
        context["url"] = f"/core{fs.url(name)}"
    return render(request, "core/upload.html", context)
