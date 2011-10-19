from django.db import models
from django.db.models.fields import DecimalField, ForeignKeyField
from django.utils.translation import ugettext as _

from mimir.models.area import Area

# Represents a location in a map.
class Location(models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    area = ForeignKeyField(Area, verbose_name=_("Area"));
    x = DecimalField()
    y = DecimalField()
