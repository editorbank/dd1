import os
import re


def read_lines_from_file(filename:str, **kw):
  if os.path.isfile(filename):
    with open(filename,'r', **kw) as f:
      return [re.sub(r"(\n|\r\n|\r)$","",line) for line in f.readlines()]
  else:
    return []