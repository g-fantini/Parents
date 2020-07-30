# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path("insertPerson/", views.insertPerson, name="Insert Person"),
    path("personsList/", views.personsList.as_view(), name="Person List"),
]