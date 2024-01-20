"""
URL configuration for coachingideas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from exercise import views as exercise_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", exercise_views.home, name="home"),
    path("exercise_table/", exercise_views.exercise_list, name="exercise_table"),
    path("about/", exercise_views.about, name="about"),
    path("exercise/", include("exercise.urls")),
    path("accounts/", include("accounts.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
