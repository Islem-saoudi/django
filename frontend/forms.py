from django import forms
from frontend.models import FrontendContact



class FrontendContactForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FrontendContactForm, self).__init__(*args, **kwargs)
        self.fields['Full_name'].widget.attrs.update({'class': 'form-control mb-30'})
        self.fields['Email'].widget.attrs.update({'class': 'form-control mb-30'})
        self.fields['Topics'].widget.attrs.update({'class': 'form-control mb-30'})
        self.fields['Message'].widget.attrs.update({'class': 'form-control mb-30'})

    class Meta:
        model = FrontendContact
        fields = "__all__"
        
