from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Teacher, ExtraLesson, Student
from .forms import TeacherForm, LessonForm, EnrollmentForm

# ГОЛОВНА (ЗАНЯТТЯ)
def index(request):
    if request.method == 'POST' and request.user.is_staff:
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    lessons = ExtraLesson.objects.all()
    form = LessonForm() if request.user.is_staff else None
    return render(request, 'school_admin/index.html', {
        'lessons': lessons, 
        'form': form
    })

# ВИКЛАДАЧІ
def teacher_list(request):
    if request.method == 'POST' and request.user.is_staff:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    
    teachers = Teacher.objects.all()
    form = TeacherForm() if request.user.is_staff else None
    return render(request, 'school_admin/teachers.html', {
        'teachers': teachers, 
        'form': form
    })

# УЧНІ (ОДНА ТАБЛИЦЯ)
def student_list(request):
    # Логіка для обробки форми (POST)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    
    # Логіка для відображення сторінки (GET)
    # Отримуємо всіх учнів з бази
    all_students = Student.objects.all().select_related('lesson__teacher')
    
    # Також отримуємо заняття, якщо вони потрібні для форми
    lessons = ExtraLesson.objects.all()
    form = EnrollmentForm()
    
    # Передаємо в шаблон змінну 'students' (саме її ми використовуємо в циклі {% for s in students %})
    context = {
        'students': all_students,
        'lessons': lessons,
        'form': form
    }
    return render(request, 'school_admin/students.html', context)

# --- РЕДАГУВАННЯ ТА ВИДАЛЕННЯ УЧНІВ ---
@staff_member_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = EnrollmentForm(instance=student)
    return render(request, 'school_admin/edit_form.html', {
        'form': form, 
        'title': 'Редагувати дані учня'
    })

@staff_member_required
def delete_student(request, pk):
    get_object_or_404(Student, pk=pk).delete()
    return redirect('student_list')

# --- CRUD ДЛЯ ВИКЛАДАЧІВ ТА ЗАНЯТЬ ---
@staff_member_required
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    form = TeacherForm(instance=teacher)
    return render(request, 'school_admin/edit_form.html', {'form': form, 'title': 'Редагувати викладача'})

@staff_member_required
def delete_teacher(request, pk):
    get_object_or_404(Teacher, pk=pk).delete()
    return redirect('teacher_list')

@staff_member_required
def edit_lesson(request, pk):
    lesson = get_object_or_404(ExtraLesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = LessonForm(instance=lesson)
    return render(request, 'school_admin/edit_form.html', {'form': form, 'title': 'Редагувати заняття'})

@staff_member_required
def delete_lesson(request, pk):
    get_object_or_404(ExtraLesson, pk=pk).delete()
    return redirect('index')