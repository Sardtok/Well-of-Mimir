from django.db import models
from django.db.models.fields import (SlugField, CharField,
                                     DecimalField, ForeignKeyField)
from django.utils.translation import ugettext as _

# Represents maps for an area.
# An area can be something like a building, floor or room.
class Area(models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    short_name = SlugField()
    full_name = CharField()
    image_type = SlugField()

    parent = ForeignKeyField(Map, related_name="areas", blank=True)
    height = DecimalField(blank=True)
    width = DecimalField(blank=True)
    x = DecimalField(blank=True)
    y = DecimalField(blank=True)
