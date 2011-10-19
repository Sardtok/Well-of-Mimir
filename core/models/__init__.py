# Note that it's important to always use absolute names for modules
# otherwise a module can get imported twice screwing up views!
# This was a problem in a Devilry plug-in I participated in earlier.
from mimir.core.models.course import Course
from mimir.core.models.oracle import Oracle
from mimir.core.models.area import Area
from mimir.core.models.location import Location
from mimir.core.models.computer import Computer
from mimir.core.models.queueplacement import QueuePlacement
