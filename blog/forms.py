from django import forms
from blog.models import Category, Blog
from django.utils.translation import gettext_lazy as _


class AddUpdateBlogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUpdateBlogForm, self).__init__(*args, **kwargs)
        self.fields['Title'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['FeatureImage'].widget.attrs.update({'class': 'hidden'})
        self.fields['Content'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['Category'].widget.attrs.update({'class': 'font-medium text-gray-900 dark:text-gray-300', })

    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['AuthorId']
        widgets = {
            "Category": forms.CheckboxSelectMultiple(),
        }

class AddUpdateCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUpdateCategoryForm, self).__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['FeatureImage'].widget.attrs.update({'class': 'hidden'})

    class Meta:
        model = Category
        fields = '__all__'
        

        