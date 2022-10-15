
from .dd1_num_bin import *
from .dd1_num_dec import *
from .dd1_num_oct import *
from .dd1_num_hex import *
from .dd1_www import *
from .dd1_date import *
from .dd1_main import *

from .detectors import detector_group, detector_regexp, detector_count, detector_unique, detector_pytype
from re import compile

_EXTRACT_NAME_P = "id" # имя или номер группы в регулярном выражении значение которой будет идентификатором детектора
_EXTRACT_NAME_RE = "^(?:DD1_)(?P<id>[0-9a-zA-Z_]+)$" 

def detectors_regexp_by_mask(d:dict, maks: str = r"^(.+)$", group_id = 0):
  compiled_mask = compile(maks)
  detectors = []
  for key in d.keys():
    m = compiled_mask.match(key)
    if m and type(d[key]) == str:
      detectors.append(detector_regexp(m.group(group_id),d[key]))
  return detectors

def make_global_detector()->detector_group:
  return detector_group(
    detector_count(),
    detector_unique(),
    detector_pytype(),
    *(detectors_regexp_by_mask(globals(), _EXTRACT_NAME_RE, _EXTRACT_NAME_P))
  )

GLOBAL_DETECTOR = make_global_detector()

def alltags()->set:
  return GLOBAL_DETECTOR.ids()
