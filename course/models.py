from django.db import models

# Create your models here.
class Course(models.Model):
    """Базовая модель курса"""
    title = models.CharField(max_length=50, verbose_name='Название курса')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['-published']

class Category(models.Model):
    """Категория курса"""
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']