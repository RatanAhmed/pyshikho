from django.db import models

# Create your models here.

class Questions():
    title = models.TextField()
    description = models.TextField()
    solution = models.TextField()
    
    def __str__(self):
        return self.title