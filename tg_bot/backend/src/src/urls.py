"""
URL configuration for src project.

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from words import views as word_views
from lessons import views as lesson_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("random/", word_views.RandomWord.as_view()),
    path("new_word/", word_views.NewWord.as_view()),
    path("lessons/", lesson_view.LessonsTable.as_view()),
    path("new_lesson/", lesson_view.NewLesson.as_view()),
]
