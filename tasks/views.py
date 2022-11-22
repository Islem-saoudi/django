from django.shortcuts import render, redirect
from tasks.models import Tasks
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.edit import DeleteView
# from django.views.generic.base import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.paginator import Paginator
from django.urls import reverse_lazy
from tasks.forms import AddUpdateTasksForm

class UpdatePostProjectView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model= Tasks
    template_name= 'backend/tasks/add_update.html'
    success_message = _('Your project has been successfully update')
    fields='__all__'


class ListPostProjectView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model= Tasks
    template_name= 'backend/tasks/list_tasks.html'
    paginate_by= 5

    
    
class DeletePostProjectView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model= Tasks
    template_name= 'backend/tasks/delete.html'
    success_message = _('Your project has been successfully deleted')