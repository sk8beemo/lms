from django.db import models

# Create your models here.
class Course(models.Model):
    """Базовая модель курса"""
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField(null=True, blank=True)