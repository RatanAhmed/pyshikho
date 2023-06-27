from django.contrib import admin
from questions.models import Questions, Learn
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import Questions

class QuestionsAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Learn)