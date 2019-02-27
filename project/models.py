# Django
from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    """
    Project model
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='user_projects',on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
