from django.urls import path
from projects import views

urlpatterns = [
    path("myspace/projects/add/", views.AddProjectView.as_view(), name="add-project"),
    path("myspace/projects/list/", views.ListProjectView.as_view(), name="list-project"),
    path("myspace/projects/update/<slug>/", views.UpdateProjectView.as_view(), name="update-project"),
    path("myspace/projects/delete/<slug>/", views.DeleteProjectView.as_view(), name="delete-project"),


    
 
]