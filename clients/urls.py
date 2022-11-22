from django.urls import path
from clients import views

urlpatterns = [
    path("myspace/clients/confirmation/", views.ClientProfileView, name="confirmation-client"),
    path("myspace/clients/list/", views.ListClientsView.as_view(), name="list-client"),
         
]