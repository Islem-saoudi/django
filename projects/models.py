from django.db import models
from django.utils.translation import gettext_lazy as _ 

from clients.models import Clients
from autoslug import AutoSlugField
from django.urls import reverse
from ckeditor.fields import RichTextField




class Projects(models.Model):
    ClientId = models.ForeignKey(Clients, on_delete=models.CASCADE)
    Name = models.CharField(_("Name"), max_length=200)
    slug = AutoSlugField(_("slug"), populate_from="Name", unique=True)
    Description = RichTextField()

    class ProjectType (models.TextChoices):
        MOBILE = "DevMob", _("Mobile Application")
        WEB = "DevWeb", _("Web Site")
        DESIGN = "Des", _("Design")
        MARKETING = "MarSEO", _("SEO & Marketing")
        DEBUGING = "Deb", _("Debuging")
    ProjectTypes = models.CharField(choices=ProjectType.choices, max_length=10)

    

    class ProjectProgress (models.TextChoices):
        IN_PROGRESS = "Progress", _("In Progress")
        DONE = "Done", _("Done")
        PENDING = "Pend", _("Pending")

    Progress = models.CharField(choices=ProjectProgress.choices, max_length=10)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})
    
