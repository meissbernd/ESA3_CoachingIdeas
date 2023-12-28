from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("upload/", views.upload, name="upload"),
    path("books/", views.book_list, name="book_list"),
    path("books/upload/", views.upload_book, name="upload_book"),
]

# add a path to core/media (to have access to local stored files)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
