from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('title', 'is_completed', 'created_at')
    search_fields = ('title', 'id')
    date_hierarchy = 'created_at'
    ordering = ('title', 'description')