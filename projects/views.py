from django.shortcuts import render, redirect
from projects.models import Projects
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.edit import DeleteView
# from django.views.generic.base import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.paginator import Paginator
from django.urls import reverse_lazy
from projects.forms import AddUpdateProjectsForm


class AddProjectView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model= Projects
    form_class = AddUpdateProjectsForm
    template_name= 'backend/projects/add_update.html'
    success_message = _('Your project has been successfully added')    
    success_url = reverse_lazy('list-project')

    # def form_valid(self, form):
    #     form.instance.ClientId = self.request.user
    #     return super().form_valid(form)


class UpdateProjectView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model= Projects
    form_class = AddUpdateProjectsForm
    template_name= 'backend/projects/add_update.html'
    success_message = _('Your project has been successfully update')
    success_url = reverse_lazy('list-project')

    # def form_valid(self, form):
    #     form.instance.AuthorId = self.request.user
    #     return super().form_valid(form)


class ListProjectView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model= Projects
    template_name= 'backend/projects/list_projects.html'
    paginate_by= 5

    
    
class DeleteProjectView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Projects
    template_name = 'backend/projects/list_projects.html'
    success_url = reverse_lazy('list-project')
    success_message = _('Your post has been successfully deleted')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteProjectView, self).delete(request, *args, **kwargs)


class ProjectsDetailView(DetailView):
    model = Projects
    template_name = "backend/projects/details.html"


