from django.contrib import admin
from .models import Teacher, ExtraLesson, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')
    search_fields = ('last_name',)

@admin.register(ExtraLesson)
class ExtraLessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ('teacher',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'school_class', 'lesson')
    list_filter = ('school_class', 'lesson')