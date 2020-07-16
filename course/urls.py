from django.urls import path

from .views import CourseList, by_category, CourseCreateView


urlpatterns = [
    path("add/", CourseCreateView.as_view(), name='add'),
    path("<int:category_id>/", by_category, name='by_category'),
    path("", CourseList, name='index'),
]