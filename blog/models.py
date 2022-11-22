from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django_quill.fields import QuillField
from sorl.thumbnail import ImageField
from django.urls import reverse
from ckeditor.fields import RichTextField



class Category (models.Model):
    Name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="Name", unique=True)
    FeatureImage = models.ImageField(blank=True, null=True, upload_to='blog/categories/%Y/%m/%d/', default='default-thumb.png')

    def __str__(self):
        return self.Name


class Blog (models.Model):
    AuthorId = models.ForeignKey(User, on_delete=models.CASCADE)
    FeatureImage = ImageField(_('Feature Image'), blank=True, null=True, upload_to='blog/%Y/%m/%d/', default='default-thumb.png')
    Title = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from="Title", unique_with='CreatedDate__month')
    slug = AutoSlugField(populate_from="Title", unique=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Content = RichTextField()
    Category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})
