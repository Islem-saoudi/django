from django import forms
from clients.models import Clients
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm, PasswordField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class UserSetting(UserChangeForm):
    password= None
    def __init__(self, *args, **kwargs):
        super(UserSetting, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['last_name'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', })
        self.fields['email'].widget.attrs.update({'class':  'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',})

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email')

class AddUpdateClientsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUpdateClientsForm, self).__init__(*args, **kwargs)
        
        self.fields['Company_name'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['Company_domaine'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', })
        self.fields['Validated_client'].widget.attrs.update({'class':  'font-medium text-gray-900 dark:text-gray-300',})


    class Meta:
        model = Clients
        
        exclude = ['user']
        fields = '__all__'