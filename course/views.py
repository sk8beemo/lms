from django.shortcuts import render
from django.http import HttpResponse

from .models import Course


def CourseList(request):
    """Вывод список всех созданных курсов"""
    text = 'Список курсов\r\n\r\n\r\n'
    for course in Course.objects.order_by('-title'):
        text +=  course.title + '\r\n' + course.description + '\r\n\r\n'
    return HttpResponse(text, content_type='text/plain; charset= utf-8')