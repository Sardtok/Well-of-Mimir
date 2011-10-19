from django.db import models
from django.db.models import (SlugField, CharField,
                                     DecimalField, ForeignKey)
from django.utils.translation import ugettext as _

# Represents maps for an area.
# An area can be something like a building, floor or room.
class Area(models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    short_name = SlugField()
    full_name = CharField(max_length=50)
    image_type = SlugField()

    parent = ForeignKey('self', related_name="areas", blank=True)
    height = DecimalField(max_digits=5, decimal_places=4, blank=True)
    width = DecimalField(max_digits=5, decimal_places=4, blank=True)
    x = DecimalField(max_digits=5, decimal_places=4, blank=True)
    y = DecimalField(max_digits=5, decimal_places=4, blank=True)
