from asyncio import tasks
from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField

from projects.models import Projects


class Tasks (models.Model):
    ProjectId = models.OneToOneField(
        Projects, on_delete=models.CASCADE, primary_key=True,)
    slug = AutoSlugField(populate_from="name",
                         unique_with='created_at', unique=True)

    class TaskType (models.TextChoices):
        NORMAL = "Nrml", _("Normal")
        WEB = "DW", _("Web Site")
        DESIGN = "Des", _("Design")
        MARKETING = "MSEO", _("SEO & Marketing")
        DEBUGING = "Deb", _("Debuging")
    Description = models.CharField(_("Description"), max_length=300)
    Delivery_date = models.DateField(_("Delivery Date")),

    class TaskAssigned (models.TextChoices):
        IT_SERVICES = "ITS", _("It Services")
        MARKETING = "MS", _("Marketing Services")
        COMMERCIAL = "CS", _("Commercial")

    ProjectTypes = models.CharField(choices=TaskType.choices, max_length=10)
    AssignedTo = models.CharField(choices=TaskAssigned.choices, max_length=10)


    # class TaskProgress (models.Model):
    #     TaskId = models.ForeignKey(tasks, on_delete=models.CASCADE)
    #     class TaskProgress (models.TextChoices):
    #         IN_PROGRESS = "Progress", _("In Progress")
    #         DONE = "Done", _("Done")
    #         PENDING = "Pend", _("Pending")
    #         Description = models.CharField(max_length= 200)
    #         Notes = models.CharField(max_length= 100)

    #     Progress = models.CharField(choices= TaskProgress.choices, max_length= 10)
