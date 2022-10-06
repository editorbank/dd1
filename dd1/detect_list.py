from .detect_str import alltags, detect_str

def set_intersection(a:set, b:set):
  return [ i for i in a if i in b ]

def detect_list(values:list):
  if len(values)==1:
    d1 = sorted(detect_str(values[0]))
    return {"all": d1, "meets": d1}
  else:
    all = detect_str(values[0])
    meets = all
    for value in values[1:]:
      d1 = detect_str(value)
      all = set_intersection(all, d1)
      meets.update(d1)
  return {"all": sorted(all), "meets": sorted(list(meets))}
