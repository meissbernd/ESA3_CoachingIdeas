from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from core.models import Book
from core.forms import BookForm


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


def book_list(request):
    books = Book.objects.all()
    return render(request, "core/book_list.html", {"books": books})


def upload_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "core/upload_book.html", {"form": form})
