from django.db import models

# Create your models here.

class Questions(models.Model):
    title = models.TextField(null=True)
    slug = models.TextField(null=True)
    description = models.TextField(null=True)
    solution = models.TextField(null=True)
    search_count = models.IntegerField(null=True)
    is_input_required = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title