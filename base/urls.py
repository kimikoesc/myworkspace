from django.urls import path
from .views import WorkspaceList, WorkspaceTasks, WorkspaceCreate, WorkspaceUpdate, WorkspaceDelete, TaskCreate, TaskUpdate, TaskDelete
 
urlpatterns = [
    path('', WorkspaceList.as_view(), name="workspacelist"),
    path('workspace/', WorkspaceTasks.as_view(), name="view-workspace"),
    path('workspace/new', WorkspaceCreate.as_view(), name="new-workspace"),
    path('workspace/<int:pk>/edit', WorkspaceUpdate.as_view(), name="edit-workspace"),
    path('workspace/<int:pk>/delete', WorkspaceDelete.as_view(), name="delete-workspace"),
    path('tasks/new', TaskCreate.as_view(), name="new-task"),
    path('tasks/<int:pk>/edit', TaskUpdate.as_view(), name="edit-task"),
    path('tasks/<int:pk>/delete', TaskDelete.as_view(), name="delete-task"),
    ]  