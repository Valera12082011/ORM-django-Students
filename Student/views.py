from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

def students(req):
    if(req.method == "GET"):
        students_list = Student.objects.all()
        return render(request=req , template_name='students.html' , context={'students': students_list})
    
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth_day = request.POST.get('data_of_birth_day')
        print(date_of_birth_day)
        group_number = request.POST.get('group_number')
        
        # Створюємо нового студента та зберігаємо його в базі даних
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            data_of_birth_day=date_of_birth_day,
            group_number=group_number
        )
        
        return HttpResponse("<h1>OK</h1>")   # Перенаправляємо на список студентів після додавання
    
    return render(request, 'add_student.html')


def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


def update_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.data_of_birth_day = request.POST.get('data_of_birth_day')
        student.group_number = request.POST.get('group_number')
        student.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)