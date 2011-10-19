from django.db import models
from django.utils.translation import ugettext as _

from mimir.core.models.location import Location

# A computer registered in the system with a location
class QueuePlacement(models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Queue placement")
        verbose_plural = _("Queue placements")

    location = ForeignKeyField(Location, verbose_name=_("Location"))
    course = ForeignKeyField(Course, verbose_name=_("Course"), blank=True)
    oracle = ForeignKeyField(Oracle, related_name="questions", verbose_name=_("Oracle"), blank=True)
    status = IntField()
    user = ForeignKeyField(User, related_name="queue_placements", verbose_name=_("User"));
