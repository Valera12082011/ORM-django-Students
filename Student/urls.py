from django.urls import path
from . import views

urlpatterns = [
    path("student_list/" , views.students ,name='students_list'),
    path("add/",views.add_student , name='add'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
]