from django import forms
from tasks.models import Tasks
from django.utils.translation import gettext_lazy as _




class AddUpdateTasksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUpdateTasksForm, self).__init__(*args, **kwargs)
        self.fields['ProjectId'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['TaskTypes'].widget.attrs.update({'class': 'font-medium text-gray-900 dark:text-gray-300', })
        self.fields['Description'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['ProjectTypes'].widget.attrs.update({'class': 'font-medium text-gray-900 dark:text-gray-300', })
        self.fields['AssignedTo'].widget.attrs.update({'class': 'font-medium text-gray-900 dark:text-gray-300', })


    class Meta:
        model = Tasks
        fields = '__all__'
        


        

        
