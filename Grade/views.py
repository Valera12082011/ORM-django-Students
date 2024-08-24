from django.shortcuts import render, get_object_or_404, redirect
from .models import Grade
from Student.models import Student
from Subject.models import Subject

# List of grades
def grade_list(request):
    grades = Grade.objects.all()
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'grade_list.html', {
        'grades': grades, 
        'students_list': students, 
        'subjects_list': subjects
    })

# Create a new grade
def create_grade(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    
    print(students)
    print(subjects)

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        grade_value = request.POST.get('grade')

        if student_id and subject_id and grade_value:
            student = Student.objects.get(id=student_id)
            subject = Subject.objects.get(id=subject_id)
            grade = Grade(student=student, subject=subject, grade=grade_value)
            grade.save()
            return redirect('grade_list')  # Перенаправлення до списку оцінок після створення нового запису

    return render(request, 'create_grade.html', {
        'students': students,
        'subjects': subjects,
    })
# Update an existing grade
def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    
    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        grade_value = request.POST.get('grade')

        grade.student = get_object_or_404(Student, pk=student_id)
        grade.subject = get_object_or_404(Subject, pk=subject_id)
        grade.grade = int(grade_value)
        grade.save()
        return redirect('grade_list')
    
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'grade_form.html', {'grade': grade, 'students': students, 'subjects': subjects})

# Delete a grade
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    
    return render(request, 'grade_confirm_delete.html', {'grade': grade})


def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')  # Перенаправлення після видалення

    return render(request, 'delete_grade.html', {'grade': grade})


def update_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        grade_value = request.POST.get('grade')

        if student_id and subject_id and grade_value:
            grade.student = Student.objects.get(id=student_id)
            grade.subject = Subject.objects.get(id=subject_id)
            grade.grade = grade_value
            grade.save()
            return redirect('grade_list')  # Перенаправлення після оновлення

    return render(request, 'update_grade.html', {
        'grade': grade,
        'students': students,
        'subjects': subjects
    })
