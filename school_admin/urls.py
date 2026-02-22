from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lesson/edit/<int:pk>/', views.edit_lesson, name='edit_lesson'),
    path('lesson/delete/<int:pk>/', views.delete_lesson, name='delete_lesson'),
    
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/edit/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    
    path('students/', views.student_list, name='student_list'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
]