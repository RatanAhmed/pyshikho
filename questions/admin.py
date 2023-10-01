from django.contrib import admin
from questions.models import Questions, Learn, LearnCodes
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import Questions

class QuestionsAdmin(SummernoteModelAdmin):
    list_per_page = 100

    # list_display = ("title", "solution")
    list_display = ("title",)
    summernote_fields = ('description', )

class LearnAdmin(SummernoteModelAdmin):
    list_per_page = 100

    SummernoteModelAdmin.description = "description | safe"
    list_display = ("title",)
    # list_display = ("title", "codes")
    summernote_fields = ('description', )
# class LearnCodeAdmin(SummernoteModelAdmin):
#     summernote_fields = ('codes', )

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Learn, LearnAdmin)
admin.site.register(LearnCodes)
# admin.site.register(LearnCodes, LearnCodeAdmin)