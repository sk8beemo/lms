from django.urls import path

from .views import CourseListView, by_category, CourseCreateView, CourseDetailView, LessonCreateView, CourseUpdateView, \
    LessonUpdateView, CourseDeleteView, LessonDetailView, LessonDeleteView

urlpatterns = [
    path("add_course/", CourseCreateView.as_view(), name='add_course'),
    path("edit_course/<int:pk>/", CourseUpdateView.as_view(), name='edit_course'),
    path("delete_course/<int:pk>/", CourseDeleteView.as_view(), name='delete_course'),
    path("<int:course_id>/", CourseDetailView, name='course_detail'),
    path("add_lesson/<int:pk>/", LessonCreateView.as_view(), name='add_lesson'),
    path("edit_lesson/<int:pk>/", LessonUpdateView.as_view(), name='edit_lesson'),
    path("lesson/<int:lesson_id>/", LessonDetailView, name='lesson_detail'),
    path("category/<int:category_id>/", by_category, name='by_category'),
    path("delete_lesson/<int:pk>/", LessonDeleteView.as_view(), name='delete_lesson'),
    path("", CourseListView, name='index'),
]