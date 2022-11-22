from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from page.models import Page 
from page.forms import AddUpdatePageForm, DetailPageForm
from django.urls import reverse_lazy


class AddPageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Page
    template_name = 'backend/page/add_update.html'
    success_message = _('Terms & Conditions has been successfully added')
    form_class = AddUpdatePageForm
    success_url = reverse_lazy('list-page')




class UpdatePageView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Page   
    template_name = 'backend/page/add_update.html'
    success_message = _('Terms & Conditions has been successfully update')
    form_class = AddUpdatePageForm
    success_url = reverse_lazy('list-page')

    def form_valid(self, form):
        form.instance.AuthorId = self.request.user
        return super().form_valid(form)

class DetailPageView(SuccessMessageMixin, DetailView):
    model = Page   
    template_name = 'frontend/page/details.html'
    form_class = DetailPageForm

class ListPageView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Page
    template_name = 'backend/page/list_page.html'
    paginate_by = 5


class DeletePageView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Page
    template_name = 'backend/page/delete.html'
    success_url = reverse_lazy('list-page')
    success_message = _('Your page has been successfully deleted')
   



