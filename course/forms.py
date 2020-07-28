from django.forms import ModelForm, Textarea

from .models import Course, Lesson


class CourseForm(ModelForm):
    """Форма создания нового курса"""
    class Meta:
        model = Course
        fields = ('title', 'description', 'category')


class LessonCreateForm(ModelForm):
    """Форма создания нового урока"""
    class Meta:
        model = Lesson
        fields = ('title', 'description')