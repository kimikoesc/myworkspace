from django.urls import path
from .views import WorkspaceList, WorkspaceTasks, WorkspaceCreate, WorkspaceUpdate, WorkspaceDelete, TaskCreate, TaskUpdate, TaskDelete, Login, SignUp
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),

    path('', WorkspaceList.as_view(), name="workspacelist"),
    path('workspace/', WorkspaceTasks.as_view(), name="view-workspace"),
    path('workspace/new', WorkspaceCreate.as_view(), name="new-workspace"),
    path('workspace/<int:pk>/edit', WorkspaceUpdate.as_view(), name="edit-workspace"),
    path('workspace/<int:pk>/delete', WorkspaceDelete.as_view(), name="delete-workspace"),
    path('tasks/new', TaskCreate.as_view(), name="new-task"),
    path('tasks/<int:pk>/edit', TaskUpdate.as_view(), name="edit-task"),
    path('tasks/<int:pk>/delete', TaskDelete.as_view(), name="delete-task"),
    ]  