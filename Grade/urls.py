from django.urls import path
from . import views

urlpatterns = [
    path('', views.grade_list, name='grade_list'),
    path('create/', views.create_grade, name='grade_create'),
    path('<int:pk>/update/', views.grade_update, name='grade_update'),
    path('<int:pk>/delete/', views.grade_delete, name='grade_delete'),
    path('delete/<int:grade_id>/', views.delete_grade, name='delete_grade'),  # Видалення оцінки
    path('update/<int:grade_id>/', views.update_grade, name='update_grade'),  # Оновлення оцінки
]
