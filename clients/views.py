from django.shortcuts import render, redirect
from clients.forms import AddUpdateClientsForm
from clients.models import Clients
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.edit import DeleteView
# from django.views.generic.base import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clients.forms import AddUpdateClientsForm, UserSetting


class AddClientsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Clients
    template_name = 'backend/clients/profile.html'
    success_message = _('Client has been successfully added')
    form_class = AddUpdateClientsForm
    success_url = reverse_lazy('list-Client')


# class UpdateClientsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Clients
#     template_name = 'backend/clients/profile.html'
#     success_message = _('Client has been successfully update')
#     fields = '__all__'


@login_required
def ClientProfileView(request):
    template_name = 'backend/clients/profile.html'

    if request.method == 'POST':
        form1 = UserSetting(request.POST, instance=request.user)
        form2 = AddUpdateClientsForm(request.POST, instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, _("Your information has been successfully updated"))

            # sender = request.user
            # recipient = User.objects.filter(is_superuser=True)
            # message = _('New cusomer account is waiting for confirmation')
            # notify.send(sender=sender, recipient=recipient, verb='Message',
            # description='New cusomer account is waiting for confirmation', level='light')
            return redirect('dashboard')
    else:
        form1 = UserSetting()
        form2 = AddUpdateClientsForm()
    if request.method == 'GET':
        form1 = UserSetting(instance=request.user)
        form2 = AddUpdateClientsForm(instance=request.user.profile)
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, template_name, context)


class ListClientsView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Clients
    template_name = 'backend/clients/list-client.html'
    paginate_by = 5


class DeleteClientsView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Clients
    template_name = 'backend/clients/delete.html'
    success_message = _('Client has been successfully deleted')


class ClientsView(DetailView):
    model = Clients
    template_name = "backend/clients/details.html"
