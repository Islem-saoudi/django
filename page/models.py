from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django.urls import reverse
from ckeditor.fields import RichTextField


class Page(models.Model):
    
    title= models.CharField(max_length=50)
    description=RichTextField()
    slug=AutoSlugField(populate_from="title", unique=True)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("detail_page", kwargs={"slug": self.slug})

