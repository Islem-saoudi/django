from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from backend.forms import PasswordChangeForm
from django.urls import reverse_lazy


class MySpaceViews(LoginRequiredMixin, TemplateView):
    template_name = "backend/index.html"


class HistoryViews(TemplateView):
    template_name = "backend/clients/history.html"


class ProfileViews(TemplateView):
    template_name = "backend/clients/profile.html"


class MarketingFormViews(TemplateView):
    template_name = "backend/support/marketing_form.html"


class MarketingListViews(TemplateView):
    template_name = "backend/support/marketing_list.html"


class TechnicalFormViews(TemplateView):
    template_name = "backend/support/technical_form.html"


class TechnicalListViews(TemplateView):
    template_name = "backend/support/technical_list.html"


class UpdateTasksViews(TemplateView):
    template_name = "backend/tasks/add_update.html"


class CheckTasksViews(TemplateView):
    template_name = "backend/tasks/check_task.html"


class SignInViews(TemplateView):
    template_name = "backend/account/login.html"


class SignUpViews(TemplateView):
    template_name = "backend/account/logout.html"


class PasswordChangeViews(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password-edit')
    template_name= "backend/password_change.html"
