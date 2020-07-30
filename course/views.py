from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Course, Category, Lesson
from .forms import CourseCreateForm, LessonCreateForm

def CourseListView(request):
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

def CourseDetailView(request, course_id):
    """Возвращаем список уроков из курса"""
    lessons = Lesson.objects.filter(course = course_id)
    course = Course.objects.get(pk= course_id)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'course/course.html', context)

class CourseCreateView(CreateView):
    """Форма создания курса"""
    template_name = 'course/create.html'
    form_class = CourseCreateForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['categories'].required = False
        return context


class CourseUpdateView(UpdateView):
    """Редактирование Курса"""
    model = Course
    fields = ['title', 'description', 'category']
    template_name_suffix = '_update_form'


class CourseDeleteView(DeleteView):
    """Удаление курса"""
    model = Course
    success_url = reverse_lazy('index')


class LessonCreateView(View):
    """Форма создания нового урока"""
    def post(self, request, pk):
        if request.method == 'POST':
            form = LessonCreateForm(request.POST)
            course = Course.objects.get(pk= pk)
            if form.is_valid():
                form = form.save(commit=False)
                form.course = course
                form.save()
            return redirect(course.get_absolute_url())
        else:
            form = LessonCreateForm()
            return render(request, 'course/course.html', dict(form=form))


class LessonUpdateView(UpdateView):
    """Редактирование Урока"""
    model = Lesson
    fields = ['title', 'description']
    template_name_suffix = '_update_form'


class LessonDeleteView(DeleteView):
    """Удаление урока"""
    model = Lesson
    success_url = reverse_lazy('index')

def LessonDetailView(request, lesson_id):
    """Возвращает список элементов урока"""
    lesson = Lesson.objects.get(pk=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'course/lesson.html', context)