from django import forms
from .models import Teacher, ExtraLesson, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {'last_name': 'Прізвище', 'first_name': 'Ім’я', 'middle_name': 'По батькові', 'description': 'Опис'}

class LessonForm(forms.ModelForm):
    class Meta:
        model = ExtraLesson
        fields = '__all__'
        labels = {'name': 'Назва заняття', 'teacher': 'Викладач', 'description': 'Опис гуртка'}

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'age', 'school_class', 'lesson']
        labels = {'full_name': 'ПІБ учня', 'age': 'Вік', 'school_class': 'Клас', 'lesson': 'Оберіть гурток'}