from django.contrib import admin
from .models import Teacher, ExtraLesson, Student

# Налаштування заголовків (Завдання 1)
admin.site.site_header = "Система управління HobbyHub"
admin.site.site_title = "Адміністратор HobbyHub"
admin.site.index_title = "Панель керування гуртками та учнями"

# Інлайн для учнів у гуртках (Завдання 4)
class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

# Власна дія (Завдання 5)
@admin.action(description="Оновити вибрані записи")
def custom_refresh(modeladmin, request, queryset):
    queryset.update()
    modeladmin.message_user(request, "Дані успішно оновлено.")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')
    search_fields = ('last_name', 'first_name')
    list_filter = ('last_name',)

@admin.register(ExtraLesson)
class ExtraLessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ('teacher',)
    search_fields = ('name',)
    inlines = [StudentInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'lesson', 'school_class', 'age')
    list_filter = ('lesson', 'school_class')
    search_fields = ('full_name',)
    actions = [custom_refresh]