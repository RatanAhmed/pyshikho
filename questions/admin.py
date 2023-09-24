from django.contrib import admin
from questions.models import Questions, Learn
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import Questions

class QuestionsAdmin(SummernoteModelAdmin):
    list_per_page = 25

    # list_display = ("title", "solution")
    list_display = ("title", "description")
    prepopulated_fields = {'description': ('description',)}
    summernote_fields = ('description', )
class LearnAdmin(SummernoteModelAdmin):
    list_per_page = 25

    SummernoteModelAdmin.description = "description | safe"
    list_display = ("title",)
    # list_display = ("title", "codes")
    summernote_fields = ('description', )
    
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Learn, LearnAdmin)