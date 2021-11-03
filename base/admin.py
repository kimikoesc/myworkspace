from django.contrib import admin
from .models import Workspace, WorkspaceUser, Tasks

# Register your models here.
admin.site.register(Workspace)
admin.site.register(WorkspaceUser)
admin.site.register(Tasks)
