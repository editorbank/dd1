import collections
from .const import KEY_UNIQUE
from .detect_value import detect_value

def detect_list(values:list):
  unique = set()
  ret = collections.OrderedDict()

  for value in values:
    unique.add(value)
    cur = detect_value(value)
    for i in cur:
      ret[i] = ret[i] + cur[i] if i in ret else cur[i]
  ret[KEY_UNIQUE]=len(unique)
  return ret
