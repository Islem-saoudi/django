from django.shortcuts import render, redirect
from blog.models import Category, Blog
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from blog.forms import AddUpdateBlogForm, AddUpdateCategoryForm


class AddPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    template_name = 'backend/blog/add_update.html'
    success_message = _('Your post has been successfully added')
    form_class = AddUpdateBlogForm
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        form.instance.AuthorId = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = AddUpdateBlogForm
    template_name = 'backend/blog/add_update.html'
    success_message = _('Your post has been successfully update')
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        form.instance.AuthorId = self.request.user
        return super().form_valid(form)


class ListPostView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Blog
    template_name = 'backend/blog/articles.html'
    paginate_by = 5


class DeletePostView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'backend/blog/delete.html'
    success_url = reverse_lazy('blog-list')
    success_message = _('Your post has been successfully deleted')


class AddCategoryView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'backend/blog/categories.html'
    success_message = _('Your category has been successfully added')
    form_class = AddUpdateCategoryForm
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        return super(AddCategoryView, self).get_context_data(**kwargs)


class UpdateCategoryView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'backend/blog/categories.html'
    success_message = _('Your category has been successfully update')
    form_class = AddUpdateCategoryForm
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        return super(UpdateCategoryView, self).get_context_data(**kwargs)


class DeleteCategoryView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'backend/blog/delete.html'
    success_message = _('Your category has been successfully deleted')
    success_url = reverse_lazy('categories')
