from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workspace(models.Model):
    workspace_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

class WorkspaceUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True);

class Tasks(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True);
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']