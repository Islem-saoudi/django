from enum import unique
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Clients(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile')
    Company_name = models.CharField(_("Company Name"), max_length=200)
    Company_domaine = models.CharField(_("Company Domain"), max_length=200)
    Validated_client = models.BooleanField(default=False)

    def __str__(self):
        return self.Company_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Clients.objects.create(user=instance)
    instance.profile.save()





