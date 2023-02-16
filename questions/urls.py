from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='questions'),
    path('questions/create', views.create, name='questions.create'),
]