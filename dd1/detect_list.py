from .detect_str import detect_str

def list_and(a:list, b:list):
  return [ i for i in a if i in b ]

def detect_list(values:list):
  if len(values)==1:
    return detect_str(values[0])
  else:
    res = detect_str(values[0])
    for one_detect in values[1:]:
      res = list_and(res, detect_str(one_detect))
  return res