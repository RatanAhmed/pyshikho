from django.conf.urls import url
from django.urls import path
from questions import views

urlpatterns = [
    path('', views.try_it, name='questions'),
    path('create/', views.create, name='questions.create'),
    path('about/', views.about, name='questions.about'),
]