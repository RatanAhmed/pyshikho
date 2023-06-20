from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('search/',views.search),
    path('learn-python/',views.learn_python),
    path('practice-python/',views.questions),
    path("try/<int:id>/", views.try_it),
    path('learn/<int:id>', views.learn_by_id),
    path('practice/<int:id>', views.practice_by_id),
    path('result/<int:id>', views.result),
]
