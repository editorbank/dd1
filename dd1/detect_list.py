import collections
from .detectors import detector

def detect_list(detector: detector, values:list):
  detector.reset()
  for value in values:
    detector.value(value)
  return collections.OrderedDict(sorted(detector.result().items()))
