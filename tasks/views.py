from django.http import Http404
from django.shortcuts import render ,get_object_or_404

# Create your views here.
# tasks/views.py
# from rest_framework import generics
from .models import Task
# from .serializers import TaskSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django_filters.rest_framework import DjangoFilterBackend
# # API برای لیست کردن همه وظایف
# class TaskListAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['is_completed']
#
# # API برای مشاهده جزئیات یک وظیفه خاص
# class TaskDetailAPIView(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         is_completed = self.request.query_params.get('is_completed')
#         if is_completed is not None:
#             queryset = queryset.filter(is_completed=(is_completed.lower() == 'true'))
#         return queryset
#
# class TaskCompleteToggleAPIView(APIView):
#     def post(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk)
#             task.is_completed = not task.is_completed
#             task.save()
#             return Response({"message": "Task completion status toggled."}, status=status.HTTP_200_OK)
#         except Task.DoesNotExist:
#             return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

def task_main(request):
    # صفحه اصلی با دو لینک برای "تمام تسک‌ها" و "تسک‌های تکمیل شده"
    return render(request, 'tasks/task/main.html')
def task_list(request):
    tasks = Task.objects.all()
    return render(
        request,
        'tasks/task/list.html',
        {'tasks': tasks}
    )
def task_completed(request):
    tasks_completed=Task.completed.all()

    return render(
        request,
        'tasks/task/completed_list.html',
        {'tasks': tasks_completed}
    )


def task_detail(request, task_id):
    # try:
    #     task = Task.objects.get(id=task_id)
    #
    # except Task.DoesNotExist:
    #     raise Http404("Task not found")

    task = get_object_or_404(Task, id=task_id, is_completed=True )

    return render(
        request,
        'tasks/task/detail.html',
        {'task': task}
    )

def task_detail_all(request, task_id):
    # try:
    #     task = Task.objects.get(id=task_id)
    #
    # except Task.DoesNotExist:
    #     raise Http404("Task not found")

    task = get_object_or_404(Task, id=task_id )

    return render(
        request,
        'tasks/task/detail.html',
        {'task': task}
    )