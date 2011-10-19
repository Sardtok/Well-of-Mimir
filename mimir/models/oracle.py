from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from mimir.models.course import Course

# Data about an oracle/TA in the system
class Oracle (models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Oracle")
        verbose_plural = _("Oracles")

    user = ForeignKeyField(User, related_name="oracles", verbose_name=_("User"))
    courses = ManyToManyField(Course, related_name="oracles", verbose_name=_("Courses"), blank=True)
