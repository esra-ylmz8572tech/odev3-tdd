from django.urls import path

from students.views import search


urlpatterns = [path("", search, name="student-search")]
