from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('questions/',views.questions),
    path('try/{id}/', views.try_it),
    path('result/', views.result),
]
