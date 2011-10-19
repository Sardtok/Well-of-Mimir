from django.db import models
from django.db.models import CharField
from django.utils.translation import ugettext as _

# Represents courses that students can ask questions about
class Course(models.Model):
    class Meta:
        app_label = "mimir"
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
    
    # Length was arbitrarily chosen - may be extended in the future
    name = CharField(max_length=50)
