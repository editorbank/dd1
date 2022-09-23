import re
from .dd1_num_bin import *
from .dd1_num_dec import *
from .dd1_num_oct import *
from .dd1_num_hex import *
from .dd1_ip import *

_DD1_NAME_TEMPLATE = re.compile("^DD1_([0-9A-Z_]+)$")

def extact_name(dd1_name:str):
  return _DD1_NAME_TEMPLATE.match(dd1_name)[1]

def dd1_names():
  return [k for k in globals() if _DD1_NAME_TEMPLATE.match(k)]

symptoms = { extact_name(k):re.compile(globals()[k]) for k in dd1_names()}

def detect(value:str)->list:
  diagnosis = []
  for k in symptoms:
    if symptoms[k].match(value):
      diagnosis.append(k)
  return diagnosis
