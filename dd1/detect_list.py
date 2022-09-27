from .detect_str import alltags, detect_str

def set_intersection(a:set, b:set):
  return [ i for i in a if i in b ]

def detect_list(values:list):
  if len(values)==1:
    return detect_str(values[0])
  else:
    res = detect_str(values[0])
    for one_detect in values[1:]:
      res = set_intersection(res, detect_str(one_detect))
  return res