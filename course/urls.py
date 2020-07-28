from django.urls import path

from .views import CourseList, by_category, CourseCreateView, LessonList, LessonCreateView


urlpatterns = [
    path("add/", CourseCreateView.as_view(), name='add'),
    path("<int:course_id>/", LessonList, name='LessonList'),
    path("add_lesson/<int:pk>/", LessonCreateView.as_view(), name='add_lesson'),
    path("category/<int:category_id>/", by_category, name='by_category'),
    path("", CourseList, name='index'),
]