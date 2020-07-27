from django.forms import ModelForm, forms

from .models import Course


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ('title', 'description', 'category')