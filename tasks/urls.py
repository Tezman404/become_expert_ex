# tasks/urls.py
from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.task_main, name='task_main'),  # لیست تمام وظایف
    path('all/', views.task_list, name='task_list'),  # لیست تمام وظایف
    path('completed/', views.task_completed, name='task_completed'),  # لیست وظایف کامل‌شده
    path('<int:task_id>/', views.task_detail_all, name='task_detail_all'),  # جزئیات هر وظیفه بدون فیلتر
    path('completed/<int:task_id>/', views.task_detail, name='task_detail'),  # جزئیات وظایف کامل‌شده
]
