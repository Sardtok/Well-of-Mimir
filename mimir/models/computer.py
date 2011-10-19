from django.db import models
from django.utils.translation import ugettext as _

from mimir.models.location import Location

# A computer registered in the system with a location
class Computer(models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Computer")
        verbose_plural = _("Computers")

    location = ForeignKeyField(Location, related_name="computer", verbose_name=_("Location"))

    # I'd like to do conversion to int, as it requires less space to store,
    # but it requires processing as we get the IP as a string
    # A database lookup by string is probably optimized so much
    # that it will still be faster to use the string directly,
    # but I will try both and profile it.
    ip4 = CharField(max_length=15)
    name = SlugField()

