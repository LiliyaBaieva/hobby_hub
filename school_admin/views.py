from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Teacher, ExtraLesson, Student
from .forms import TeacherForm, LessonForm, EnrollmentForm

# ГОЛОВНА (ЗАНЯТТЯ) з пошуком
def index(request):
    query = request.GET.get('q')
    if query:
        lessons = ExtraLesson.objects.filter(name__icontains=query)
    else:
        lessons = ExtraLesson.objects.all()

    if request.method == 'POST' and request.user.is_staff:
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    form = LessonForm() if request.user.is_staff else None
    return render(request, 'school_admin/index.html', {
        'lessons': lessons, 
        'form': form,
        'query': query
    })

# ВИКЛАДАЧІ з пошуком
def teacher_list(request):
    query = request.GET.get('q')
    if query:
        teachers = Teacher.objects.filter(last_name__icontains=query) | Teacher.objects.filter(first_name__icontains=query)
    else:
        teachers = Teacher.objects.all()

    if request.method == 'POST' and request.user.is_staff:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    
    form = TeacherForm() if request.user.is_staff else None
    return render(request, 'school_admin/teachers.html', {
        'teachers': teachers, 
        'form': form,
        'query': query
    })

# УЧНІ з пошуком та фільтрацією
def student_list(request):
    query = request.GET.get('q')
    lesson_id = request.GET.get('lesson')
    
    students = Student.objects.all().select_related('lesson__teacher')
    
    if query:
        students = students.filter(full_name__icontains=query)
    if lesson_id:
        students = students.filter(lesson_id=lesson_id)

    if request.method == 'POST' and request.user.is_staff:
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    
    lessons = ExtraLesson.objects.all()
    form = EnrollmentForm()
    
    return render(request, 'school_admin/students.html', {
        'students': students,
        'lessons': lessons,
        'form': form,
        'query': query,
        'selected_lesson': lesson_id
    })

# --- РЕДАГУВАННЯ ТА ВИДАЛЕННЯ ---

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
    return render(request, 'school_admin/edit_form.html', {'form': form, 'title': 'Редагувати учня'})

@staff_member_required
def delete_student(request, pk):
    get_object_or_404(Student, pk=pk).delete()
    return redirect('student_list')

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

# САМЕ ЦІЄЇ ФУНКЦІЇ У ТЕБЕ НЕ ВИСТАЧАЛО:
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