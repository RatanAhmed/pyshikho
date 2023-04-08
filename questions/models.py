from django.db import models

# Create your models here.

class Questions(models.Model):
    title = models.TextField()
    slug = models.TextField(null=True)
    description = models.TextField()
    # solution = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " " + self.description