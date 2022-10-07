import re
from .dd1_num_bin import *
from .dd1_num_dec import *
from .dd1_num_oct import *
from .dd1_num_hex import *
from .dd1_www import *
from .dd1_date import *
from .dd1_main import *

_extact_name_re = re.compile("^DD1_([0-9A-Z_]+)$")

def _extact_name(dd1_name:str):
  return _extact_name_re.match(dd1_name)[1]

def dd1_tags()->set:
  return {k for k in globals() if _extact_name_re.match(k)}

def alltags()->set:
  return [_extact_name(k) for k in dd1_tags()]

symptoms = { _extact_name(k):re.compile(globals()[k]) for k in dd1_tags()}

def detect_value(value:any)->set:
  ret = {type(value).__name__}
  for k in symptoms:
    if symptoms[k].match(f"{value}"):
    # if symptoms[k].search(f"{value}"):
      ret.add(k)
  return ret
