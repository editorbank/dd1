from .detect_value import detect_value

def set_intersection(a:set, b:set):
  return [ i for i in a if i in b ]

def detect_list(values:list):
  if len(values)==1:
    d1 = sorted(detect_value(values[0]))
    return {"all": d1, "meets": []}
  else:
    all = detect_value(values[0])
    meets = all
    for value in values[1:]:
      d1 = detect_value(value)
      all = set_intersection(all, d1)
      meets.update(d1)
  return {"all": sorted(all), "meets": sorted([i for i in meets if i not in all])}
