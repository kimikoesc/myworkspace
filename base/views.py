from django.shortcuts import render
from django.views.generic.list import ListView # GET all
from django.views.generic.detail import DetailView # GET specific
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView # POST request
from django.urls import reverse_lazy # redirects user to a different page

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Tasks, Workspace # User should already be logged in after register


# Create your views here.

class WorkspaceList(ListView):
    model = Workspace
    context_object_name = "workspaces"

class WorkspaceTasks(ListView):
    model = Tasks
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selectedWorkspace = self.request.GET.get('id')
        if selectedWorkspace:
            context['tasks'] = context['tasks'].filter(workspace=selectedWorkspace)
            return context