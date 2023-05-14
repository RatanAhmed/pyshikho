from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('search/',views.search),
    path('questions/',views.questions),
    path('try/<int:id>', views.try_it),
    path('result/<int:id>', views.result),
]
