from django.db import models

# Create your models here.

class Questions(models.Model):
    title = models.TextField(null=True)
    slug = models.TextField(null=True)
    description = models.TextField(null=True)
    solution = models.TextField(null=True)
    search_count = models.IntegerField(null=True)
    is_input_required = models.IntegerField(null=False)
    learn_or_practice = models.IntegerField(null=False,default=0, help_text="0=Learn, 1=practice")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta():
        verbose_name_plural = 'Questions'

class Learn(models.Model):
    title = models.TextField(null=True)
    slug = models.TextField(null=True)
    description = models.TextField(null=True)
    codes = models.TextField(null=True)
    search_count = models.IntegerField(null=True)
    is_input_required = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class LearnCodes(models.Model):
    learn = models.ForeignKey(Learn, on_delete=models.CASCADE)
    link = models.CharField(max_length=50, verbose_name='Identifier', null=True)
    codes = models.TextField(null=True)
    def __str__(self):
        return self.link
    class Meta:
        verbose_name_plural = "Learn Codes"