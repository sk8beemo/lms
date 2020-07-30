from django.contrib import admin

from .models import Course, Category, Lesson

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'published')
    list_display_links = ( 'title', 'description' )
    search_fields = ('title', 'description')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'description')
    list_display_links = ('title', 'course')
    sortable_by = ('course')
    search_fields = ('title', 'course')

admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Lesson, LessonAdmin)
