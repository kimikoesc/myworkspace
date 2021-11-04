from django.shortcuts import render, redirect
from django.views.generic.list import ListView # GET all
from django.views.generic.detail import DetailView # GET specific
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView # POST request
from django.urls import reverse_lazy, reverse # redirects user to a different page

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Tasks, Workspace # User should already be logged in after register


# Create your views here.

class Login(LoginView):
    template_name = 'base/login.html'
    redirect_authenticated_user = True
    fields = '__all__'
    
    # Once the user succesfully logs in, redirect to tasks
    def get_success_url(self) -> str:
        return reverse_lazy('workspacelist')

class SignUp(FormView):
    template_name = 'base/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('workspacelist') 

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUp, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if (self.request.user.is_authenticated):
            return redirect('tasks')
        return super(SignUp, self).get(*args, **kwargs);


class WorkspaceList(LoginRequiredMixin, ListView):
    model = Workspace
    context_object_name = "workspaces"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workspaces'] = context['workspaces'].filter(users=self.request.user)
        return context

class WorkspaceTasks(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = "allTasks"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selectedWorkspace = self.request.GET.get('id')
        selectedWorkspaceName = self.request.GET.get('name')
        if selectedWorkspace:
            context['allTasks'] = context['allTasks'].filter(workspace=selectedWorkspace)
            context['myTasks'] = context['allTasks'].filter(assigned_to=self.request.user)
            context['workspace'] = selectedWorkspaceName
            context['workspaceID'] = selectedWorkspace
            return context

class WorkspaceCreate(LoginRequiredMixin, CreateView):
    model = Workspace
    fields = "__all__"
    success_url = reverse_lazy('workspacelist')

class WorkspaceUpdate(LoginRequiredMixin, UpdateView):
    model = Workspace
    fields = "__all__"
    success_url = reverse_lazy('workspacelist')

class WorkspaceDelete(LoginRequiredMixin, DeleteView):
    model = Workspace
    context_object_name = 'workspace'
    success_url = reverse_lazy('workspacelist') 

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = "__all__"

    def get_success_url(self):
        selectedWorkspace = self.request.GET.get('id')
        selectedWorkspaceName = self.request.GET.get('name')
        res = reverse_lazy('view-workspace') + f'?id={selectedWorkspace}&name={selectedWorkspaceName}'
        return res
        
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ['assigned_to', 'title', 'description', 'complete']

    def get_success_url(self):
        selectedWorkspace = self.request.GET.get('id')
        selectedWorkspaceName = self.request.GET.get('name')
        res = reverse_lazy('view-workspace') + f'?id={selectedWorkspace}&name={selectedWorkspaceName}'
        return res

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Tasks
    context_object_name = 'task'

    def get_success_url(self):
        selectedWorkspace = self.request.GET.get('id')
        selectedWorkspaceName = self.request.GET.get('name')
        res = reverse_lazy('view-workspace') + f'?id={selectedWorkspace}&name={selectedWorkspaceName}'
        return res
