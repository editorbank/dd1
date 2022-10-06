import csv
from dd1.detect_list import detect_list

def dict_set_values_from(a:dict,b:dict)->dict:
  for i in a:
    if i in b:
      a[i]=b[i]
  return a

def get_if_exists(keys:tuple, d:dict)->dict:
  return {k:d[k] for k in keys if k in d}

file_options = ("newline", "encoding")
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

def _all_csv_by_cols(filename:str,**options):
  with open(filename,"r",**get_if_exists(file_options,options)) as f:
    reader = csv.DictReader(f,**get_if_exists(reader_options, options))
    ret = {header:[] for header in reader.fieldnames}
    for row in reader:
      for header in ret: 
        ret[header].append(row[header])
    return ret

def detect_dict_of_lists(in_dict: dict):
  return { k:detect_list(in_dict[k]) for k in in_dict }

def detect_csv(**options):
  d = _all_csv_by_cols(**options)
  # print(d)
  return {"filename":options["filename"], "fields":{ k:detect_list(d[k]) for k in d }}
