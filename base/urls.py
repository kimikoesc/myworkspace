from django.urls import path
from .views import WorkspaceList, WorkspaceTasks
 
urlpatterns = [
    path('', WorkspaceList.as_view(), name="workspacelist"),
    path('workspace/', WorkspaceTasks.as_view(), name="view-workspace")
    ]  