# Django
from django.contrib.auth.models import User
from django.db import models

# local Django
from project.models import Project


class Task(models.Model):
    """
    Task model
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True, null=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, blank=True, null=True,on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
