import csv

from .detectors import detector
from .detect_list import detect_list

def filter_key_for(keys:tuple, d:dict)->dict:
  return {k:d[k] for k in keys if k in d}

file_options = (
  "newline",
  "encoding",
)
reader_options = (
  "delimiter",
  "quotechar",
  "escapechar",
  "doublequote",
  "skipinitialspace",
  "lineterminator",
  "quoting",
  "strict",
)
escaped_options = file_options + reader_options

def _all_csv_by_cols(filename:str,**options):
  with open(filename,"r",**filter_key_for(file_options,options)) as f:
    reader = csv.DictReader(f,**filter_key_for(reader_options, options))
    ret = {header:[] for header in reader.fieldnames}
    for row in reader:
      for header in ret:
        ret[header].append(row[header])
    return ret

def detect_csv(detector:detector=detector(), **options):
  d = _all_csv_by_cols(**options)
  return { k:detect_list(detector, d[k]) for k in d }
