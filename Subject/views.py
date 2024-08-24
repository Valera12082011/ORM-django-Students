from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject

def get_all_subject(req):
    if req.method == 'GET':
        list_subject = Subject.objects.all()
        return render(req, 'list_subject.html', context={'subjects': list_subject})

def add_new_subject(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        code = req.POST.get('code')
        if name and code:
            new_subject = Subject(name=name, code=code)
            new_subject.save()
            return redirect('get_all_subject')  # Redirect to the list view after adding the subject
    return render(req, 'add_subject.html')  # Render the form template if GET request or invalid data

def delete_subject(req, subject_id):
    if req.method == 'POST':
        subject = get_object_or_404(Subject, id=subject_id)
        subject.delete()
        return redirect('get_all_subject')  # Redirect to the list view after deletion

def update_subject(req, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if req.method == 'POST':
        name = req.POST.get('name')
        code = req.POST.get('code')
        if name and code:
            subject.name = name
            subject.code = code
            subject.save()
            return redirect('get_all_subject')  # Redirect to the list view after updating the subject
    return render(req, 'update_subject.html', context={'subject': subject})  # Render the form with the current data
