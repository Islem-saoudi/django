from email.message import Message
from django.db import models
from django.utils.translation import gettext_lazy as _

class FrontendContact (models.Model):
    Full_name= models.CharField(_("Full Name"), max_length=100)
    Email= models.EmailField(_("Email"), max_length=200)
    Topics= models.CharField(_("Topics"), max_length= 250)
    Message= models.TextField(_("Message"))


    def __str__(self):
        return self.Full_name
    
        