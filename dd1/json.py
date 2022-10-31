import json
import os
from .const import *
from .detectors import *

class DetectorJSONEncoder(json.JSONEncoder):
  def default(self, o: detector) -> any:
    return o.to_serializable() if issubclass(type(o),detector) else super().default(o)

_all_serializable_detectors = {i.__name__:i for i in (
  detector_count,
  detector_regexp,
  detector_type,
  detector_unique,
  detector_group
)}

class DetectorJSONDecoder(json.JSONDecoder):
  def __init__(self, *args, **kwargs):
    super().__init__(object_hook = self.object_hook, *args, **kwargs)

  def object_hook(self, dct:dict):
    if CLASS_KEY in dct:
      _class_name = dct[CLASS_KEY]
      dct.pop(CLASS_KEY)
      if _class_name in _all_serializable_detectors:
        return (_all_serializable_detectors[_class_name])(**dct)
    return dct

def dumps(obj:detector,*a,**kw):
  return json.dumps(obj,*a,cls=DetectorJSONEncoder, **kw)

def loads(s,*a,**kw)->detector:
  return json.loads(s,*a,cls=DetectorJSONDecoder, **kw)

def dump(obj:detector,fp,*a,**kw):
  return json.dump(obj,fp,*a,cls=DetectorJSONEncoder, **kw)

def load(fp,*a,**kw)->detector:
  return json.load(fp,*a,cls=DetectorJSONDecoder, **kw)

### Schema Load and Save to JSON format ###

file_options = (
  "newline",
  "encoding",
  )

dump_options = (
  "skipkeys",
  "ensure_ascii",
  "check_circular",
  "allow_nan",
  "indent",
  "separators",
  "default",
  "sort_keys",
  )

dumpf_options = dump_options + file_options

def dumpf(obj:detector, filename:str,**options):
  if os.path.isfile(filename):
    return f"""File "{filename}" allredy exists!"""
  else:
    with open(filename,'w',**{k:v for k,v in options.items() if k in file_options}) as fp:
      dump(obj,fp,**{k:v for k,v in options.items() if k in dump_options})
      return f"""Schema saved to file: "{filename}"."""

def loadf(filename:str,**options)->detector:
  if not os.path.isfile(filename):
    return {}
  else:
    with open(filename,'r',**{k:v for k,v in options.items() if k in file_options}) as fp:
      return load(fp,**{k:v for k,v in options.items() if k in dump_options})