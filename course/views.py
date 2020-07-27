from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Course, Category
from .forms import CourseForm

def CourseList(request):
    """Контроллер возвращает словарь всех курсов"""
    courses = Course.objects.all()
    categories = Category.objects.all()
    context = {'courses': courses, 'categories': categories}
    return render(request, 'course/index.html', context)

def by_category(request, category_id):
    """Список курсов по категории"""
    courses = Course.objects.filter(category = category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'courses': courses, 'categories': categories, 'current_category': current_category}
    return render(request, 'course/by_category.html', context)


class CourseCreateView(CreateView):
    template_name = 'course/create.html'
    form_class = CourseForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['categories'].required = False
        return context