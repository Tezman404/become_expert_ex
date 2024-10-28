from django.db import models


class completed_manager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(is_completed=True)
        )

# Create your models here.
class Task(models.Model):



    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    completed = completed_manager()

    def __str__(self):
        return f"{self.title} - {'Completed' if self.is_completed else 'Pending'}"

