# Note that it's important to always use absolute names for modules
# otherwise a module can get imported twice screwing up views!
# This was a problem in a Devilry plug-in I participated in earlier.
from mimir.models.course import Course
from mimir.models.oracle import Oracle
from mimir.models.area import Area
from mimir.models.location import Location
from mimir.models.computer import Computer
from mimir.models.queueplacement import QueuePlacement
