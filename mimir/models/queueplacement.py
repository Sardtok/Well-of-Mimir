from django.db import models
from django.db.models import ForeignKey, IntegerField
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from mimir.models.location import Location
from mimir.models.course import Course
from mimir.models.oracle import Oracle

# A computer registered in the system with a location
class QueuePlacement(models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Queue placement")
        verbose_name_plural = _("Queue placements")

    location = ForeignKey(Location, verbose_name=_("Location"))
    course = ForeignKey(Course, verbose_name=_("Course"), blank=True)
    oracle = ForeignKey(Oracle, related_name="questions", verbose_name=_("Oracle"), blank=True)
    status = IntegerField()
    user = ForeignKey(User, related_name="queue_placements", verbose_name=_("User"));
