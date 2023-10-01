from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from questions import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('search/',views.search),
    path('learn-python/',views.learn_python,),
    path('learn-python/<int:id>/',views.learn_view),
    path('practice-python/',views.questions),
    path('practice-python/<int:id>/',views.practice_view),
    path("try/<int:id>/", views.try_it),
    path("learn-python/<int:learn_id>/try-it/<identifier>/", views.learn_try_it),
    path('learn/<int:id>', views.learn_by_id),
    path('practice/<int:id>', views.practice_by_id),
    path('result/<int:id>', views.result),
    path('summernote/', include('django_summernote.urls')),
    path('editor/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
