from django.db import models


# Create your models here.
class Task(models.Model):
    Tasktitle=models.CharField(max_length=25)
    Taskdesc=models.TextField(max_length=255)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Tasktitle