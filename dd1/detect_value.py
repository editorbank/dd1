import collections
from .main_detector import GLOBAL_DETECTOR

def detect_value(value:any)->set:
  dt = GLOBAL_DETECTOR
  dt.reset()
  dt.value(value=value)
  return collections.OrderedDict(sorted(dt.result().items()))
