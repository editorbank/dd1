import collections
from .main_detector import GLOBAL_DETECTOR

def detect_list(values:list):
  dt = GLOBAL_DETECTOR
  dt.reset()
  for value in values:
    dt.value(value)
  return collections.OrderedDict(sorted(dt.result().items()))


