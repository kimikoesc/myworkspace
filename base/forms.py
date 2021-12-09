from django import forms
from .models import Tasks, WorkspaceUser, Workspace # User should already be logged in after register


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['assigned_to', 'title', 'description', 'complete']

    def __init__(self, *args, **kwargs):
        wpUser = kwargs.pop('wpUser', None)
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = WorkspaceUser.objects.filter(workspace=wpUser)