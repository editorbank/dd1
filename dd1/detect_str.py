import re
from .dd1_num_bin import *
from .dd1_num_dec import *
from .dd1_num_oct import *
from .dd1_num_hex import *
from .dd1_www import *
from .dd1_date import *

_extact_name_re = re.compile("^DD1_([0-9A-Z_]+)$")

def _extact_name(dd1_name:str):
  return _extact_name_re.match(dd1_name)[1]

def dd1_names():
  return [k for k in globals() if _extact_name_re.match(k)]

symptoms = { _extact_name(k):re.compile(globals()[k]) for k in dd1_names()}

def detect_str(value:str)->list:
  diagnosis = []
  for k in symptoms:
    if symptoms[k].match(value):
      diagnosis.append(k)
  return sorted(diagnosis)
