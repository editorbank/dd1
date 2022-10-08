import re
import collections

from .const import KEY_LEN
from .dd1_num_bin import *
from .dd1_num_dec import *
from .dd1_num_oct import *
from .dd1_num_hex import *
from .dd1_www import *
from .dd1_date import *
from .dd1_main import *
_EXTRACT_NAME_RE = re.compile("^DD1_([0-9A-Z_]+)$")

def _extact_name(dd1_name:str):
  return _EXTRACT_NAME_RE.match(dd1_name)[1]

def dd1_tags()->set:
  return {k for k in globals() if _EXTRACT_NAME_RE.match(k)}

def alltags()->set:
  return [_extact_name(k) for k in dd1_tags()]

symptoms = { _extact_name(k):re.compile(globals()[k]) for k in dd1_tags()}

def detect_value(value:any)->set:
  ret = {type(value).__name__:1, KEY_LEN:1}
  for k in symptoms:
    if symptoms[k].match(f"{value}"):
      ret[k]=1
  return collections.OrderedDict(sorted(ret.items()))
