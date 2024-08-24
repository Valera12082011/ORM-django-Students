from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_subject, name='get_all_subject'),  # Відображення списку предметів
    path('add/', views.add_new_subject, name='add_subject'),  # Додавання нового предмета
    path('delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),  # Видалення предмета
    path('update/<int:subject_id>/', views.update_subject, name='update_subject'),  # Оновлення предмета
]
